# Task Game 
Aplicação com objetivo de ajudar empresas e pessoas a se organizarem de forma divertida.
Utilizaremos Flask e react para o desenvolvimento desse projeto
[Repositorio front-end](https://github.com/Task-Game/task-game-front)

Email para contato: [tcctaskgame@gmail.com](tcctaskgame@gmail.com)

# Dependencias usadas
- [Flask](https://flask.palletsprojects.com/en/1.1.x)
- [Requests](https://requests.readthedocs.io/en/master/)
- [Flask-Scripts](https://flask-script.readthedocs.io/en/latest/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## Documentação interna
- Swaager

## Estrutura da Aplicação
- app (Pasta principal)
    - app/api (Controla as rotas e a regra de negocio de cada um)
        - app/api/Item
        - app/api/Tarefa
        - app/api/Usuario
        - app/api/Foo
        - app/api/__init__.py
    - api/data (Camada de dados da aplicação/estrutura do banco)
        - app/data/models (Contem os models, controla o banco)
        - app/data/models/__init__.py
        - app/data/models/SqlStructure.py (Estutura do banco)
- __init__.py
- manager.py (Controla as migrations Ex.: ```$ python3 manager.py bd init``` # Inicia a migration)
- config.py (Configurações do ambiente do projeto)
- runner.py (Roda a aplicação)

## Para rodar o projeto

**NÃO RODAR COMO ADMIN**
1. ```$ python3 -m venv .venv```
2. ```$ source .venv/bin/activate```
3. ```$ pip install -t requirements.txt```
4. ```$ python main.py```

## Rodar migrations
**VERIFICAR SE A VERSÃO DO PYTHON**(tem que ser ^3.6.~)
1. Crie o banco de dados no seu pc, seja pelo comando SQL ou pelo workbench
    ```create database <nome_do_banco>```
2. Criar arquivo '.env' utilizando o '.env.exemple' como modelo
3. Alterar os valores para os de seu ambiente
5. ```$ python manager.py migrade```
6. ```$ python manager.py upgrade```
7. Abrir o seu banco de dados e verificar se as tableas foram criadas
8. Aproveite c:

## Ciclo de alteração das migrates
1. Fazer alguma alteração no 'models.py'
2. python manager.py db migrate
3. python manager.py db upgrade
4. Volta para o passo 1 

## Rotas
### Projetos
- [x] Index(Mostrar todos)
- [x] Create(Criar novo)
- [x] Show(Mostar um espeficio)
- [x] Update(Editar um espefico)
- [x] Destroy(Deletar um especifico)
- [x] Show user per project

### Usuario
- [x] Index(Mostrar todos)
- [x] Create(Criar novo)
- [x] Show(Mostar um espeficio)
- [x] Update(Editar um espefico)
- [x] Destroy(Deletar um especifico)
- [x] Show task per user

### Tarefas
- [x] Index(Mostrar todos)
- [x] Create(Criar novo)
- [x] Show(Mostar um espeficio)
- [x] Update(Editar um espefico)
- [x] Destroy(Deletar um especifico)
- [x] Show user in task

### Item
- [x] Index(Mostrar todos)
- [x] Create(Criar novo)
- [x] Show(Mostar um espeficio)
- [x] Update(Editar um espefico)
- [x] Destroy(Deletar um especifico)
- [x] Show itens per shop

### Loja
- [x] Index(Mostrar todos)
- [x] Create(Criar novo)
- [x] Show(Mostar um espeficio)
- [x] Update(Editar um espefico)
- [x] Destroy(Deletar um especifico)

### Meta
- [x] Index(Mostrar todos)
- [x] Create(Criar novo)
- [x] Show(Mostar um espeficio)
- [x] Update(Editar um espefico)
- [x] Destroy(Deletar um especifico)
- [x] Show goals in task