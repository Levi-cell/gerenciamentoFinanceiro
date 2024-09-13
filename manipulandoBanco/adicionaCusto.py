from manipulandoDatas import funcoesResultandes as fr
from manipulandoBanco import consultaExistencia as ce
from tratandoErros import trata_entrada_de_valor
from conexaoBanco import cursor, conexao
from datetime import timedelta
import time


def adiciona_custo_semanal():

    data_inicial, data_final = fr.calcula_proximo_periodo_semanal()
    data_existente = ce.consulta_existencia_de_data(data_inicial)  # verifica existencia de data

    if data_existente is not None:

        print(f"Já foi registrado um custo para essa semana ...  no valor total de R${data_existente[3] * 6}", "\n")
        stop = False
        while not stop:
            print("Nesse caso o que deseja fazer ? \n")
            print("1 - Excluir o custo dessa semana e adicionar outro. \n"
                  "2 - Não é necessário atualização, apenas volte. \n")

            opcao = input("Digite uma das opções acima: \n")
            if opcao == "1":
                novo_custo = input("Digite o novo valor de custo dessa semana:\n")
                novo_custo = trata_entrada_de_valor(novo_custo)

                valor_antigo_deletado = """
                
                DELETE * FROM lucro_diario WHERE data_dia BETWEEN %s and %s;
                
                
                """

                cursor.execute(valor_antigo_deletado,(data_inicial, data_final,))
                conexao.commit()

                custo_diario = novo_custo/6
                day = 0
                lista_de_datas = [data_inicial]

                while len(lista_de_datas) < 6:
                    day += 1

                    data_nova = data_inicial + timedelta(days=day)
                    lista_de_datas.append(data_nova)

                    insere_valores_atualizados = """

                                INSERT INTO lucro_diario(data_dia, custo_dia)
                                VALUES (%s, %s);

                                """
                    cursor.execute(insere_valores_atualizados, (lista_de_datas[day], custo_diario,))
                    conexao.commit()
                confere_valor = """
                                SELECT * FROM lucro_diario WHERE data_dia BETWEEN %s and %s;

                                """
                cursor.execute(confere_valor, (data_inicial, data_final,))
                confere_valor = cursor.fetchall()
                for registro in confere_valor:
                    print(f"Foi adicionado um custo médio de {registro[3]} no dia {registro[1]} ")
                    return







    # lista_datas = [data_inicial]
    # day = 0
    #
    # while len(lista_datas) < 6:
    #     day += 1
    #     data_nova = data_inicial + timedelta(days=day)
    #     lista_datas.append(data_nova)
    #
    # if data_existente is not None:
    #     print(f"Já foi registrado um custo para essa semana ...  no valor de R${data_existente[3] * 6}", "\n")
    #     stop = False
    #     while not stop:
    #         print("Nesse caso o que deseja fazer ? \n")
    #         print("1 - Excluir o custo dessa semana e adicionar outro. \n"
    #               "2 - Não é necessário atualização, apenas volte. \n")
    #         opcao = input("Digite uma das opções acima: \n")
    #         if opcao == "1":
    #             novo_custo = input("Digite o novo valor de custo dessa semana:\n")
    #             novo_custo = trata_entrada_de_valor(novo_custo)
    #             # deletando datas e valores da semana
    #             vezes = 0
    #             while vezes < 6:
    #                 data_deletada = """
    #
    #             DELETE FROM lucro_diario WHERE data_dia = %s;
    #
    #             """
    #                 cursor.execute(data_deletada, (lista_datas[vezes],))
    #                 conexao.commit()
    #                 vezes += 1
    # custo = input("Olá, por favor me informe o custo da próxima semana:")
    # custo = trata_entrada_de_valor(custo)
    # custo_dia = custo / 6
