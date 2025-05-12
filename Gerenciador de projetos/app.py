# Aqui eu importo o Flask e algumas funções que vou usar pra lidar com páginas, formulários e mensagens
from flask import Flask, render_template, redirect, flash, request, url_for

# Esse aqui é o módulo pra mexer com arquivos e diretórios
import os

# Isso aqui serve pra garantir que o nome do arquivo que o usuário enviar não dê problema no sistema
from werkzeug.utils import secure_filename

# Vou usar CSV pra salvar os dados dos projetos e tarefas
import csv

# Pra trabalhar com data e hora (tipo a data que o projeto foi criado)
from datetime import datetime

# Crio o app Flask
app = Flask(__name__)

# Aqui eu defino os nomes dos arquivos CSV que vou usar pra guardar os dados
csv_projetos = "projetos.csv"
csv_tarefas = "tarefas.csv"

# Essa chave é tipo uma senha secreta pra deixar o app mais seguro (pra mensagens e sessões)
app.secret_key = os.urandom(24).hex()

# Um dicionário pra guardar variáveis que vão pros templates (tipo textos ou imagens da home)
context = {}

# Dicionário que guarda os projetos
projetos = {}

# Dicionário que guarda as tarefas separadas por projeto
tarefas_por_projeto = {}

# Função que carrega os dados dos arquivos CSV (se já existirem) e joga pra memória
def carregar_dados_csv():
    # Se o arquivo de projetos existir, eu abro e leio linha por linha
    if os.path.exists(csv_projetos):
        with open(csv_projetos, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id_projeto = int(row["id"])
                projetos[id_projeto] = {
                    "nome": row["nome"],
                    "descricao": row["descricao"],
                    "imagem": row["imagem"],
                    "data_criacao": row["data_criacao"]
                }

    # Mesmo esquema aqui, mas agora pras tarefas
    if os.path.exists(csv_tarefas):
        with open(csv_tarefas, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id_projeto = int(row["id_projeto"])
                tarefa = {
                    "id": int(row["id"]),
                    "id_projeto": id_projeto,
                    "nome": row["nome"],
                    "descricao": row["descricao"],
                    "status": row["status"]
                }
                if id_projeto not in tarefas_por_projeto:
                    tarefas_por_projeto[id_projeto] = []
                tarefas_por_projeto[id_projeto].append(tarefa)

# Essa função salva os projetos no arquivo CSV
def salvar_projetos_csv():
    with open(csv_projetos, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "nome", "descricao", "imagem", "data_criacao"])
        for id, projeto in projetos.items():
            writer.writerow([id, projeto["nome"], projeto["descricao"], projeto["imagem"], projeto["data_criacao"]])

# E essa aqui salva as tarefas
def salvar_tarefas_csv():
    with open(csv_tarefas, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "id_projeto", "nome", "descricao", "status"])
        for lista in tarefas_por_projeto.values():
            for tarefa in lista:
                writer.writerow([tarefa["id"], tarefa["id_projeto"], tarefa["nome"], tarefa["descricao"], tarefa["status"]])

# Quando o app começa, já carrega os dados que estavam salvos nos CSVs
carregar_dados_csv()

# Página inicial do site
@app.route('/')
def homepage():
    context["Inicio"] = "img/imginicio.jpg"
    context["Titulo"] = "GERENCIADOR DE PROJETOS"
    context["Texto"] = "ORGANIZE SEUS PROJETOS AQUI"
    return render_template("homepage.html", **context)

# Mostra a lista com todos os projetos
@app.route('/projetos')
def lista_projetos():
    context["projetos"] = projetos
    return render_template("lista_projetos.html", **context)

# Abre o formulário pra adicionar um novo projeto
@app.route('/add_projeto_form')
def add_projeto_form():
    return render_template('add_projeto.html', **context)

# Recebe os dados do formulário e adiciona um novo projeto
@app.route('/add_projeto', methods=['POST'])
def add_projeto():
    next_id = max(projetos.keys(), default=0) + 1  # calcula o próximo ID
    nome = request.form['nome']
    descricao = request.form['descricao']
    imagem = request.files['imagem']
    imagem_path = None

    # Se o usuário enviou uma imagem, salva ela na pasta e guarda o caminho
    if imagem:
        filename = secure_filename(imagem.filename)
        imagem.save(os.path.join('static/img', filename))
        imagem_path = f'img/{filename}'

    data_criacao = datetime.now().strftime("%Y-%m-%d")  # pega a data de hoje
    projetos[next_id] = {
        "nome": nome,
        "descricao": descricao,
        "imagem": imagem_path,
        "data_criacao": data_criacao
    }
    tarefas_por_projeto[next_id] = []  # cria uma lista vazia de tarefas pra esse projeto
    salvar_projetos_csv()
    return redirect(url_for('lista_projetos'))

# Mostra o formulário de edição de um projeto
@app.route('/edit_projeto/<int:id>', methods=['GET'])
def edit_projeto(id):
    projeto = projetos.get(id)
    if not projeto:
        flash("Projeto não encontrado.", "error")
        return redirect(url_for('lista_projetos.html'))
    return render_template("edit_projeto.html", projeto=projeto, id=id)

# Atualiza o projeto com os novos dados
@app.route('/up_projeto', methods=['POST'])
def up_projeto():
    projeto_id = int(request.form.get('id'))
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    imagem = request.files.get('imagem')

    projeto = projetos.get(projeto_id)
    if not projeto:
        flash("Projeto não encontrado.", "error")
        return redirect(url_for('lista_projetos.html'))

    projeto["nome"] = nome
    projeto["descricao"] = descricao

    if imagem and imagem.filename:
        filename = secure_filename(imagem.filename)
        imagem.save(os.path.join('static/img', filename))
        projeto["imagem"] = f'img/{filename}'

    salvar_projetos_csv()
    return redirect(url_for('ver_projeto', id=projeto_id))

# Mostra um projeto específico com todas as suas tarefas
@app.route('/projeto/<int:id>')
def ver_projeto(id):
    projeto = projetos.get(id)
    tarefas = tarefas_por_projeto.get(id, [])
    if not projeto:
        flash("Projeto não encontrado.", "error")
        return redirect(url_for('lista_projetos'))
    return render_template("projeto_tarefas.html", projeto=projeto, tarefas=tarefas, id=id)

# Adiciona uma tarefa a um projeto
@app.route('/add_tarefa/<int:id_projeto>', methods=['GET', 'POST'])
def add_tarefa(id_projeto):
    if id_projeto not in projetos:
        flash("Projeto não encontrado.", "error")
        return redirect(url_for('lista_projetos'))

    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        status = request.form['status']
        next_id = sum(len(lst) for lst in tarefas_por_projeto.values()) + 1
        tarefa = {
            "id": next_id,
            "id_projeto": id_projeto,
            "nome": nome,
            "descricao": descricao,
            "status": status
        }
        if id_projeto not in tarefas_por_projeto:
            tarefas_por_projeto[id_projeto] = []
        tarefas_por_projeto[id_projeto].append(tarefa)
        salvar_tarefas_csv()
        return redirect(url_for('ver_projeto', id=id_projeto))

    return render_template("add_tarefa.html", id_projeto=id_projeto)

# Edita uma tarefa existente
@app.route('/edit_tarefa/<int:id_projeto>/<int:id_tarefa>', methods=['GET', 'POST'])
def edit_tarefa(id_projeto, id_tarefa):
    tarefa = next((t for t in tarefas_por_projeto.get(id_projeto, []) if t["id"] == id_tarefa), None)

    if not tarefa:
        flash("Tarefa não encontrada.", "error")
        return redirect(url_for('ver_projeto', id=id_projeto))

    if request.method == 'POST':
        tarefa["nome"] = request.form['nome']
        tarefa["descricao"] = request.form['descricao']
        tarefa["status"] = request.form['status']
        salvar_tarefas_csv()
        return redirect(url_for('ver_projeto', id=id_projeto))

    return render_template("edit_tarefa.html", tarefa=tarefa, id_projeto=id_projeto, id_tarefa=id_tarefa)

# Deleta um projeto e todas as tarefas dele
@app.route('/delete_projeto/<int:id>', methods=['POST'])
def delete_projeto(id):
    if id in projetos:
        projetos.pop(id)
        tarefas_por_projeto.pop(id, None)
        salvar_projetos_csv()
        salvar_tarefas_csv()
        flash("Projeto e tarefas excluídos.", "success")
    else:
        flash("Projeto não encontrado.", "error")
    return redirect(url_for('lista_projetos'))

# Deleta uma tarefa específica
@app.route('/delete_tarefa/<int:id_projeto>/<int:id_tarefa>', methods=['POST'])
def delete_tarefa(id_projeto, id_tarefa):
    tarefa = next((t for t in tarefas_por_projeto.get(id_projeto, []) if t["id"] == id_tarefa), None)
    if tarefa:
        tarefas_por_projeto[id_projeto].remove(tarefa)
        salvar_tarefas_csv()
        flash("Tarefa excluída.", "success")
    else:
        flash("Tarefa não encontrada.", "error")
    return redirect(url_for('ver_projeto', id=id_projeto))

# Página onde o usuário pode excluir projetos
@app.route('/excluir_projetos')
def excluir_projetos():
    context["projetos"] = projetos
    return render_template("excluir_projetos.html", **context)

# Aqui é onde o app realmente roda
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # roda em modo debug e acessível por outros dispositivos na rede
