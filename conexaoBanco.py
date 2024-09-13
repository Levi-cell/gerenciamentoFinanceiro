import mysql.connector

# habilitando conexão com banco de dados.
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='filho998874_',
    database='GerenciamentoFinanceiro'
)

# habilitando cursor.
"""
Atenção, só é necessário importar a conexão caso vá deletar, atualizar e inserir dados.

Para fazer consultas não é necessário.

"""

cursor = conexao.cursor()

# fazendo testes
# cursor.execute("SELECT * FROM lucro_diario ")
#
# tabela_lucro = cursor.fetchall()
#
# print("dia / data / faturamento do dia / custo médio do dia / lucro do dia  \n")
#
# for cada_registro in tabela_lucro:
#     print("dia:", cada_registro[0],
#           "data:", cada_registro[1],
#           "faturamento do dia:", cada_registro[2],
#           "custo médio do dia:", cada_registro[3],
#           "lucro do dia ", cada_registro[4], "\n")

