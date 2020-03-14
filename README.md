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
1. ////////////

## Rotas
### Projetos
- [ ] Listas Projetos
- [ ] Adicionar Projetos
- [ ] Editar Projetos
- [ ] Deletar Projetos

### Pessoas
- [ ] Listas pessoas de projeto
- [ ] Adicionar pessoas
- [ ] Editar pessoas
- [ ] Excluir pessoas


### Tarefas
- [ ] Listar Tarefas individuais
- [ ] Listar Tarefas por projeto
- [ ] Listar Tarefas por projeto por pessoa
- [ ] Adicionar Tarefas individuais
- [ ] Adicionar Tarefas a Projeto
- [ ] Editar Tarefas
- [ ] Excluir Tarefa individual
- [ ] Excluir tarefa de projeto
