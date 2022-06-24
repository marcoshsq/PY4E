import pyodbc

"""
Passo 1: Baixar e instalar o SSMS - digitar no google download ssms e baixar 1º link
Passo 2: Instalar
Passo 3: Criar Banco de Dados, abrindo uma query e rodando:

CREATE DATABASE Nome_Banco_Dados

Passo 4: Criar tabela, usando:

USE Nome_Banco_Dados
CREATE TABLE Vendas(
    id_venda int,
    cliente varchar(50),
    produto varchar(50),
    data_venda date,
    preco decimal(6, 2),
    quantidade int,
    )

Passo 5: Adicionar 1 valor exemplo:

INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    (1, 'Lira', 'PC', '15/02/2021', 8000, 1)

"""

dados_conexao = "Driver={SQL Server};" "Server=DESKTOP-T2JV7P5;" "Database=PythonSQL;"

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()


id = 3
cliente = "Lira Python"
produto = "Carro"
data = "25/08/2021"
preco = 5000
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()
