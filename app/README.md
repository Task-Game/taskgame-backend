## Rodar servidor

**NÃO RODAR COMO ADMIN**
1. ```$ python3 -m venv .venv```
2. ```$ source .venv/bin/activate```
2. ```$ pip install --upgrade pip
3. ```$ pip install -t requirements.txt```
4. ```$ python manager run.py```

**VERIFICAR SE A VERSÃO DO PYTHON**(python > ^3.6.~)
1. Crie o banco de dados no seu pc, seja pelo comando SQL ou pelo workbench
    ```create database <nome_do_banco>```
3. Verificar em que modo estara rodando o projeto dentro de "manager.py"
5. ```$ python manager.py migrade```
6. ```$ python manager.py upgrade```
7. Abrir o seu banco de dados e verificar se as tableas foram criadas
8. Aproveite c: