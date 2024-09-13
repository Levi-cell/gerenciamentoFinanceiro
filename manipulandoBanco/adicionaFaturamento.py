from manipulandoBanco import consultaExistencia as ae
from tratandoErros import trata_entrada_de_valor
from conexaoBanco import cursor, conexao
import datetime
import time
from manipulandoDatas import funcoesResultandes as fr

def adiciona_faturamento():
    data_atual = datetime.date.today()
    dados_consultados = ae.consulta_existencia_de_data(data_atual)
    if dados_consultados is not None:
        print(f"Já foi registrado um faturamento hoje...  no valor de R${dados_consultados[2]}", "\n")
        stop = False
        while not stop:
            print("Nesse caso o que deseja fazer ? \n")
            print("1 - Excluir o faturamento de hoje e adicionar outro. \n"
                  "2 - Não é necessário atualização, apenas volte. \n")
            opcao = input("Digite uma das opções acima: \n")
            if opcao == "1":
                novo_faturamento = input("Digite o novo valor de faturamento:\n")
                novo_faturamento = trata_entrada_de_valor(novo_faturamento)
                data_deletada = """

                DELETE FROM lucro_diario WHERE data_dia = %s;

                """
                cursor.execute(data_deletada, (data_atual,))
                conexao.commit()
                insere_valores_atualizados = """

                INSERT INTO lucro_diario(data_dia, faturamento_dia, custo_dia)
                VALUES (%s, %s, %s);

                """
                cursor.execute(insere_valores_atualizados, (data_atual, novo_faturamento, dados_consultados[3],))
                conexao.commit()
                confere_valor = """
                SELECT * FROM lucro_diario WHERE data_dia = %s;

                """
                cursor.execute(confere_valor, (data_atual,))
                confere_valor = cursor.fetchone()
                print(f"O valor de R${confere_valor[2]} da data {confere_valor[1]} foi  atualizado no banco de dados! "
                      f"\n")
                time.sleep(3)
                return

            elif opcao == "2":
                stop = True
                return
    valor_faturamento = input(f"Por favor, digite o faturamento total de hoje: \n")
    valor_faturamento = trata_entrada_de_valor(valor_faturamento)
    insere_dados = """

    INSERT INTO lucro_diario(data_dia, faturamento_dia)
    VALUES ( %s, %s);

    """
    cursor.execute(insere_dados, (data_atual, valor_faturamento,))
    conexao.commit()
    print(f"O valor de R${valor_faturamento} faturado em {data_atual} foi adicionado no banco de dados \n")
    time.sleep(3)



