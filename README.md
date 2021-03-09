# Task Game 
Aplicação com objetivo de ajudar empresas e pessoas a se organizarem de forma divertida e pratica.
Utilizaremos Flask e react para o desenvolvimento desse projeto
[Repositorio front-end](https://github.com/Task-Game/task-game-front)

Email para contato: [tcctaskgame@gmail.com](tcctaskgame@gmail.com)

# Dependencias usadas
- [Flask](https://flask.palletsprojects.com/en/1.1.x)
- [Flask-Restplus](https://flask-restplus.readthedocs.io/en/stable/)
- [Flask-Scripts](https://flask-script.readthedocs.io/en/latest/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## Documentação interna
- Swaager 

## Para rodar o projeto
- Verificar README da pasta APP

## Rodar migrations
- Verificar README da pasta APP


## Ciclo de alteração das migrates
1. Fazer alguma alteração no 'models.py'
2. python manager.py db migrate
3. python manager.py db upgrade 

## Rotas
### Grupo
- [x] Index(Mostrar todos)
- [x] Create(Criar novo)
- [x] Show(Mostar um espeficio)
- [x] Update(Editar um espefico)
- [x] Destroy(Deletar um especifico)
- [x] Show user per project

### Usuario
- [x] Index(Mostrar todos "read")
- [x] Create(Criar novo "create")
- [x] Update(Editar um espefico "update")
- [x] Destroy(Deletar um especifico "delete")
- [x] Show(Mostar um espeficio "read")
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

### Meta
- [x] Index(Mostrar todos)
- [x] Create(Criar novo)
- [x] Show(Mostar um espeficio)
- [x] Update(Editar um espefico)
- [x] Destroy(Deletar um especifico)
- [x] Show goals in task
