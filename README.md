<h1 align="center">
  <br>TaskMate</h1>

<div align="center">
  
</div>

<a id="pt-readme"></a>
## [English](#en-readme) | Português

**TaskMate** é um sistema baseado em Django e Python projetado para gerenciar tarefas entre usuários de mesmo time. Ele utiliza o SQLite como banco de dados e oferece recursos como: 

- Cadastro e autenticação de usuários: o sistema permite o registro de novos usuários, além de login e logout para o controle de sessão. Cada usuário terá acesso à suas próprias tarefas, gerenciando-as de forma individual.
- Gerenciamento de tarefas: os usuários podem criar, editar e excluir tarefas. Cada tarefa é composta por um título, descrição, status e gerenciamento se é privada ou pública. As tarefas são atribuidas aos usuários do sistema, promovendo a colaboração no gerenciamento.
- Status de tarefas: indicam o progresso como "pendente", "em andamento", e "concluida".
- Dashboard: onde é possível visualizar todas as tarefas.
  
## Como rodar os códigos

Para rodar os códigos é necessária uma IDE Python como o **VSCODE**, **Pycharm** baixe o projeto e siga alguns comandos no terminal para ver a magia acontecendo!
Você pode também dar um fork no projeto e abrir com o codespaces do Github. 

<br>

## Comandos

### Configurando um Ambiente Virtual
Para criar e ativar um ambiente virtual, utilize os seguintes comandos Bash:

```bash
$ python -m venv venv 
$ source venv/bin/activate
```

Instale o Django executando o seguinte comando:

```bash
$ pip install django
```

Em seguida, inicialize o seu projeto Django:

```bash
$ django-admin startproject TaskMate .
```

Executando o Servidor:

```bash
$ python manage.py runserver 
```

Acesse a sua aplicação através do link fornecido.

### Criando um Aplicativo Django
Crie um novo aplicativo chamado "taskmate" com o seguinte comando:

```bash
$ python manage.py startapp taskmate
```

Não se esqueça de adicionar este aplicativo ao arquivo `TaskMate/settings.py` na seção "INSTALLED_APPS".

### Gerenciando Modelos de Banco de Dados
Depois de definir os modelos de dados, gere as migrações com o seguinte comando:

```bash
$ python manage.py makemigrations
```

Se as migrações foram criadas com sucesso, aplique-as ao banco de dados:

```bash
$ python manage.py migrate 
```

### Tarefas Administrativas
Para tarefas administrativas, utilize o painel de administração do Django. Para criar uma conta de superusuário, execute:

```bash
$ python manage.py createsuperuser
```

Agora, o seu sistema de gerenciamento de tarefas está configurado e pronto para uso. Personalize-o de acordo com as suas necessidades específicas.

 <br></br>

<h2 align="left" >Equipe 🧠</h2>

- Arthur Diesel (rgm)
- Gabriela Cristina Schmitt (25733150)
- Vinicius Dionizio Patrocinio (rgm)

<br></br>

✨ Obrigada pela atenção! ✨


-------
<br>
<br>

<h1 align="center">
  <br>TaskMate</h1>
<a id="en-readme"></a>

## English | [Português](#pt-readme)


**TaskMate** is a system based on Django and Python designed to manage tasks between users on the same team. It uses SQLite as its database and offers features such as: 

- User registration and authentication: the system allows the registration of new users, as well as login and logout for session control. Each user will have access to their own tasks, managing them individually.
- Task Management: Users can create, edit and delete tasks. Each task consists of a title, description, status and management whether it is private or public. Tasks are assigned to system users, promoting collaboration in management.
- Task status: indicate progress as "pending", "in progress", and "completed".
- Dashboard: where you can view all tasks.

## How to run the codes

To run the codes you need a Python IDE such as **VSCODE, Pycharm**   just download the entire project and follow the above bash commands to see magic happening! 
You can also fork the project and open it with Github codespaces.

<br>

## Getting Started

### Setting Up a Virtual Environment
To create and activate a virtual environment, use the following Bash commands:

```bash
$ python -m venv venv 
$ source venv/bin/activate
```

Install Django by running the following command:

```bash
$ pip install django
```

Next, initialize your Django project:

```bash
$ django-admin startproject TaskMate .
```

Running the Server:

```bash
$ python manage.py runserver 
```

Access your application through the provided link.


Creating a Django App
Create a new app named "taskmate" with the following command:

```bash
$ python manage.py startapp taskmate
```

Don't forget to add this app to your TaskMate/settings.py file under the "INSTALLED_APPS" section.

Managing Database Models
Once you have defined your data models, generate migrations with:

```bash
$ python manage.py makemigrations
```

If the migrations were created successfully, apply them to the database:

```bash
$ python manage.py migrate
```

Administrative Tasks
For administrative tasks, use the Django admin panel. To create a superuser account, run:

```bash
$ python manage.py createsuperuser
```

Now, your tasks system is set up and ready for use. Customize it according to your specific needs.

<br>

✨ Thanks for your attention! ✨
