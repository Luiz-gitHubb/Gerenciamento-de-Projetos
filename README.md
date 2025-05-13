# Gerenciamento-de-Projetos
Web App de Gerenciamento de Projetos
## 📖 Contexto do Projeto

---

Este sistema foi desenvolvido com **Flask (Python)** e utiliza **arquivos CSV** para armazenamento de dados.

Funcionalidades principais :

- **Gerenciamento de Projetos**: criação, visualização, edição e exclusão de projetos.
- **Gestão de Tarefas**: adição, edição e remoção de tarefas associadas a cada projeto.
- **Upload de Imagens**: possibilidade de enviar uma imagem ilustrativa para cada projeto.

---

### 🔧 Stack Tecnológico

- **Linguagem:** Python
- **Framework Web:** Flask
- **Frontend:** HTML5 + TailwindCSS
- **Armazenamento de Dados:** CSV (formato simples de banco de dados)

---

## 📋 **Requisitos Funcionais Implementados**

O sistema já permite:

- **Cadastro de Projetos** – Cada projeto possui nome, descrição e data de criação.
- **Listagem de Projetos** – O usuário consegue visualizar todos os projetos existentes.
- **Edição de Projetos** – É possível alterar o nome e a descrição de um projeto.
- **Remoção de Projetos** – O usuário pode excluir projetos, o que também apaga as tarefas associadas.
- **Adição de Tarefas aos Projetos** – Cada tarefa está vinculada a um projeto e possui título, descrição e status (Pendente, Em andamento, Concluída).
- **Edição e Remoção de Tarefas** – O sistema permite modificar ou excluir tarefas.
- **Visualização de Tarefas de um Projeto Específico** – Ao selecionar um projeto, o usuário visualiza todas as tarefas relacionadas a ele.

---

## **⚙️ Configuração do Ambiente e Estrutura do Projeto**

Este projeto utiliza **Flask (Python)** com **arquivos CSV** como solução de persistência de dados. Abaixo estão os principais passos para configuração e estruturação do ambiente:

### **Preparação do Ambiente**

---

- **Criação da pasta do projeto**
    
    Estruture uma nova pasta onde todo o conteúdo será armazenado.
    
- **Criação do ambiente virtual:**
    
    ```bash
    python -m venv venv
    ```
    
- **Ativação do ambiente virtual:**

```jsx
./venv/Scripts/Activate.ps1
```

- **Instalação do Flask e bibliotecas necessárias**
    
    ```bash
    pip install flask werkzeug
    ```
    
- **Criação do arquivo principal (`app.py`)**
    
    Responsável por definir as rotas e lógica da aplicação.
    

---

## 📂 Estrutura de Arquivos

- `app.py`: script principal da aplicação.
- `projetos.csv`: armazena dados dos projetos.
- `tarefas.csv`: armazena dados das tarefas associadas aos projetos.
- `templates/`: diretório de templates HTML.
- `static/img/`: onde as imagens dos projetos são salvas.

---

## 🔧 Funcionalidades

### 1. Homepage

- **Rota**: `/`
- **Descrição**: Página inicial com imagem e texto de introdução.
- **Template**: `homepage.html`

![home page](https://github.com/user-attachments/assets/8cb8c5dd-baf0-4bbd-b348-980e10da4f7d)


---

### 2. Listagem de Projetos

- **Rota**: `/projetos`
- **Descrição**: Mostra todos os projetos existentes.
- **Template**: `lista_projetos.html`

![image.png](attachment:467b1c0d-d13e-414d-8c24-453cb94bf2f0:image.png)

---

### 3. Adicionar Projeto

- **Rota GET**: `/add_projeto_form` (formulário)
- **Rota POST**: `/add_projeto` (envio de dados)
- **Campos**:
    - Nome
    - Descrição
    - Imagem (upload)
- **Template**: `add_projeto.html`

![image.png](attachment:46f26a0b-49c0-441e-9738-9b952b7bef0b:image.png)

---

### 4. Editar Projeto

- **Rota GET**: `/edit_projeto/<int:id>`
- **Rota POST**: `/up_projeto`
- **Template**: `edit_projeto.html`

![image.png](attachment:99919ca6-46ec-4bd5-9fcb-c9742635129e:image.png)

---

### 5. Excluir Projeto

- **Rota POST**: `/delete_projeto/<int:id>`
- Remove o projeto e todas as tarefas associadas.

![image.png](attachment:c319a70f-8887-4cd3-90b0-1a3ece7599ee:image.png)

---

### 6. Ver Projeto e suas Tarefas

- **Rota**: `/projeto/<int:id>`
- **Template**: `projeto_tarefas.html`

![image.png](attachment:65d6b6fd-60bf-4966-9d11-2b234cdfe002:image.png)

---

### 7. Adicionar Tarefa

- **Rota GET/POST**: `/add_tarefa/<int:id_projeto>`
- **Campos**:
    - Nome
    - Descrição
    - Status (ex: "Pendente", "Concluído")
- **Template**: `add_tarefa.html`

![image.png](attachment:202f21ce-4ab0-4af7-8a55-08347aef22e1:image.png)

---

### 8. Editar Tarefa

- **Rota GET/POST**: `/edit_tarefa/<int:id_projeto>/<int:id_tarefa>`
- **Template**: `edit_tarefa.html`

![image.png](attachment:d2933398-b271-41f4-b29b-2eb0901c6f74:image.png)

---

### 9. Excluir Tarefa

- **Rota POST**: `/delete_tarefa/<int:id_projeto>/<int:id_tarefa>`

![image.png](attachment:07d28914-c650-4a5f-b1a2-91902d39d412:image.png)

---

### 10. Tela de Exclusão de Projetos

- **Rota GET**: `/excluir_projetos`
- **Template**: `excluir_projetos.html`

![image.png](attachment:175cac22-9bf4-4655-ab1b-808620ff120d:image.png)

---

## 🗂️ Formatos dos Arquivos CSV

### `projetos.csv`

| id | nome | descricao | imagem | data_criacao |
| --- | --- | --- | --- | --- |

### `tarefas.csv`

| id | id_projeto | nome | descricao | status |
| --- | --- | --- | --- | --- |

---

## 🧠 Funcionalidades Internas

- **carregar_dados_csv**: Lê os CSVs e popula os dicionários `projetos` e `tarefas_por_projeto`.
- **salvar_projetos_csv / salvar_tarefas_csv**: Persistem as alterações nos arquivos CSV.
- **context**: Dicionário global para passar dados para os templates.

---

## 🔐 Segurança

- `app.secret_key` é gerada aleatoriamente com `os.urandom(24).hex()` para sessões seguras.
- `secure_filename()` é usado para salvar imagens com nomes válidos.
