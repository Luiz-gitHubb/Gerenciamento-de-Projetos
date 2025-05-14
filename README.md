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

![lista de projeto](https://github.com/user-attachments/assets/34f3fdc4-b639-4721-82b2-d20ab35fa7fc)


---

### 3. Adicionar Projeto

- **Rota GET**: `/add_projeto_form` (formulário)
- **Rota POST**: `/add_projeto` (envio de dados)
- **Campos**:
    - Nome
    - Descrição
    - Imagem (upload)
- **Template**: `add_projeto.html`
  
![adicionar projeto](https://github.com/user-attachments/assets/03c6e54e-2a11-41f6-8fe0-b5765a39a240)


---

### 4. Editar Projeto

- **Rota GET**: `/edit_projeto/<int:id>`
- **Rota POST**: `/up_projeto`
- **Template**: `edit_projeto.html`

![editar projetos](https://github.com/user-attachments/assets/cac43925-c0f4-41c3-9f49-e888f6005e9a)


---

### 5. Excluir Projeto

- **Rota POST**: `/delete_projeto/<int:id>`
- Remove o projeto e todas as tarefas associadas.

![excluir projeto](https://github.com/user-attachments/assets/81e7c712-900d-40ba-8c7a-47ec8ee32250)


---

### 6. Ver Projeto e suas Tarefas

- **Rota**: `/projeto/<int:id>`
- **Template**: `projeto_tarefas.html`

![Captura de tela 2025-05-13 211146](https://github.com/user-attachments/assets/ea51c5b9-9b55-4390-b973-c8ea78cb10e5)

---

### 7. Adicionar Tarefa

- **Rota GET/POST**: `/add_tarefa/<int:id_projeto>`
- **Campos**:
    - Nome
    - Descrição
    - Status (ex: "Pendente", "Concluído")
- **Template**: `add_tarefa.html`

![Captura de tela 2025-05-13 211225](https://github.com/user-attachments/assets/5d8c183f-132b-40cc-beac-fbd13bb7bbd2)


---

### 8. Editar Tarefa

- **Rota GET/POST**: `/edit_tarefa/<int:id_projeto>/<int:id_tarefa>`
- **Template**: `edit_tarefa.html`

![Captura de tela 2025-05-13 211342](https://github.com/user-attachments/assets/747fcaaa-1dde-4f7a-8513-e6204689f1fe)


---

### 9. Excluir Tarefa

- **Rota POST**: `/delete_tarefa/<int:id_projeto>/<int:id_tarefa>`

![Captura de tela 2025-05-13 211443](https://github.com/user-attachments/assets/5f54238d-54a7-49c5-9993-e87a20f5ffed)


---

### 10. Tela de Exclusão de Projetos

- **Rota GET**: `/excluir_projetos`
- **Template**: `excluir_projetos.html`

![Captura de tela 2025-05-13 211526](https://github.com/user-attachments/assets/84cfe8ed-d8c9-42af-95ca-75e5ca72862c)


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
