## Rodar servidor

**NÃO RODAR COMO ADMIN**
1. ```$ python3 -m venv .venv```
2. ```$ source .venv/bin/activate```
3. ```$ pip install -t requirements.txt```
4. ```$ python run.py```

**VERIFICAR SE A VERSÃO DO PYTHON**(python > ^3.6.~)
1. Crie o banco de dados no seu pc, seja pelo comando SQL ou pelo workbench
    ```create database <nome_do_banco>```
2. Criar arquivo '.env' utilizando o '.env.exemple' como modelo
3. Alterar os valores para os de seu ambiente
5. ```$ python manager.py migrade```
6. ```$ python manager.py upgrade```
7. Abrir o seu banco de dados e verificar se as tableas foram criadas
8. Aproveite c: