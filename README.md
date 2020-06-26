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

## Para rodar o projeto
- Verificar README da pasta APP

## Rodar migrations
- Verificar README da pasta APP


## Ciclo de alteração das migrates
1. Fazer alguma alteração no 'models.py'
2. python manager.py db migrate
3. python manager.py db upgrade
4. Volta para o passo 1 

## Rotas
### Projetos
- [] Index(Mostrar todos)
- [] Create(Criar novo)
- [] Show(Mostar um espeficio)
- [] Update(Editar um espefico)
- [] Destroy(Deletar um especifico)
- [] Show user per project

### Usuario
- [x] Index(Mostrar todos "read")
- [x] Create(Criar novo "create")
- [] Show(Mostar um espeficio "read")
- [x] Update(Editar um espefico "update")
- [x] Destroy(Deletar um especifico "delete")
- [] Show task per user

### Tarefas
- [] Index(Mostrar todos)
- [] Create(Criar novo)
- [] Show(Mostar um espeficio)
- [] Update(Editar um espefico)
- [] Destroy(Deletar um especifico)
- [] Show user in task

### Item
- [] Index(Mostrar todos)
- [] Create(Criar novo)
- [] Show(Mostar um espeficio)
- [] Update(Editar um espefico)
- [] Destroy(Deletar um especifico)
- [] Show itens per shop

### Loja
- [] Index(Mostrar todos)
- [] Create(Criar novo)
- [] Show(Mostar um espeficio)
- [] Update(Editar um espefico)
- [] Destroy(Deletar um especifico)

### Meta
- [] Index(Mostrar todos)
- [] Create(Criar novo)
- [] Show(Mostar um espeficio)
- [] Update(Editar um espefico)
- [] Destroy(Deletar um especifico)
- [] Show goals in task
