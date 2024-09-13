from manipulandoBanco import adicionaFaturamento as af, adicionaCusto as ac
from tratandoErros import tratamento_de_retorno, trata_entrada_de_opcao
from manipulandoDatas import funcoesResultandes as fr
from conexaoBanco import cursor, conexao
import datetime


iniciar = (input("Olá casal Lemos, Digite qualquer coisa para iniciar o programa de Gerenciamento"
                 " Financeiro do Caldeirão Nordestino: \n"))

data_atual = datetime.date.today()
data_inicial_proxima_semana, data_final_proxima_semana = fr.calcula_proximo_periodo_semanal()
parou = False
while not parou:

    print(f"1 - Consultar informações. \n"
          f"2 - Registrar faturamento do dia atual. ({data_atual}) \n"
          f"3 - Registrar custo da próxima semana. ({data_inicial_proxima_semana} - {data_final_proxima_semana}) \n"
          f"4 - Consultar todos os registros. \n"
          f"5 - Consultar faturamento, custo e lucro total da empresa.")

    menu = input("O que deseja fazer? digite uma opção dentre as acima: \n ")

    menu = trata_entrada_de_opcao(menu)

    if menu == "1":

        primeira_dia_semana, ultimo_dia_semana = fr.calcula_ultimo_periodo_semanal()
        primeiro_dia_mes, ultimo_dia_mes = fr.calcula_ultimo_periodo_mensal()
        primeiro_dia_ano, ultimo_dia_ano = fr.ultimo_periodo_anual()

        opcao = input(f" 1 - Consultar informações da semana passada: {primeira_dia_semana} até {ultimo_dia_semana}. \n"
                      f" 2 - Consultar informações do mês passado: {primeiro_dia_mes} até {ultimo_dia_mes}. \n"
                      f" 3 - Consultar informações do ano passado:  {primeiro_dia_ano} até {ultimo_dia_ano}. \n")

        opcao = trata_entrada_de_opcao(opcao)

        if opcao == "1":

            # Espaço para a função que mostrará o total de lucro, custo, e faturamento da última semana.

            nova_opcao = input("Deseja visualizar o registro de cada dia dessa semana? Digite ""sim"" ou pressione "
                               "qualquer tecla para voltar para o menu:")

            if nova_opcao == "sim":
                # Espaço para a função que irá mostrar o lucro, custo e faturamento de cada dia da semana.

                parou = tratamento_de_retorno(parou)

        elif opcao == "2":

            # Espaço para a função que mostrará o total de lucro, custo, e faturamento do último mês.

            nova_opcao = input(f"Deseja visualizar o registro de cada dia desse mês? Digite sim ou pressione "
                               "qualquer tecla para voltar para o menu:")

            if nova_opcao == "sim":
                # Espaço para a função que mostrará o lucro, custo, e faturamento de cada dia desse último mês.

                parou = tratamento_de_retorno(parou)

        elif opcao == "3":

            # Espaço para a função que mostrará o total de lucro, custo, e faturamento do ano passado.

            nova_opcao = input(f"Deseja visualizar o registro de cada mês desse ano? Digite sim ou pressione "
                               "qualquer tecla para voltar para o menu:")

            if nova_opcao == "sim":
                # Espaço para a função que mostrará o lucro, custo, e faturamento de cada mês do ano passado.

                parou = tratamento_de_retorno(parou)
        else:

            opcao_invalida = input("Você digitou uma opção inválida, pressione qualquer tecla para volta para o "
                                   "menu principal")

    elif menu == "2":

        print("")

        af.adiciona_faturamento()

        parou = tratamento_de_retorno(parou)

    elif menu == "3":

        # Espaço para a função que irá adicionar o custo no banco de dados.

        print("")

    elif menu == "4":

        # Espaço para a função que irá consultar todos os dias registrados no banco.

        print("")

    elif menu == "5":

        # Espaço para a função que irá retornar o lucro total, custo total e faturamento total da empresa até agora.

        print("")

    else:

        opcao_invalida = input("Você digitou uma opção inválida, pressione qualquer tecla para volta para o "
                               "menu principal")

cursor.close()
conexao.close()
