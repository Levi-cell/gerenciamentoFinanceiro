from manipulandoDatas import funcoesPrimarias as fp
from datetime import datetime, timedelta
import datetime


def calcula_proximo_periodo_semanal():

    """
    Essa função calcula o próximo periodo semanal
    :return: Retorna a data atual, data inicial da proxima semana, e a data final da próxima semana
    """

    data_inicial_proxima_semana = fp.verifica_proxima_ter()
    data_final_proxima_semana = data_inicial_proxima_semana + datetime.timedelta(days=5)

    return data_inicial_proxima_semana, data_final_proxima_semana


def calcula_ultimo_periodo_semanal():
    """
        Essa função calcula o último periodo semanal
        :return: Retorna a data atual, data inicial da última semana, e a data final da última semana
        """

    data_inicial_ultima_semana = fp.verificar_ter_passada()
    data_final_ultima_semana = data_inicial_ultima_semana + datetime.timedelta(days=5)

    return data_inicial_ultima_semana, data_final_ultima_semana


def calcula_ultimo_periodo_mensal():

    """
    Essa função calcula o último periodo mensal, do dia 1 até o último dia do próximo mês
    :return: Retorna a Data do primeiro dia do mês e a data do último dia do mês passado.
    """

    primeiro_dia_mes = fp.obter_primeiro_dia_mes_passado()
    ultimo_dia_mes = fp.obter_ultimo_dia_mes_passado()

    return primeiro_dia_mes, ultimo_dia_mes


def ultimo_periodo_anual():
    """
       Essa função calcula o último periodo anual, do dia 1 de janeiro do ano passado até o dia 31 do 12 do ano
       passado
       :return: Retorna a Data do primeiro dia do ano passado e a data do último dia do ano passado.
    """
    primeiro_dia_ano_ = fp.primeiro_dia_ano_passado()
    ultimo_dia_ano = fp.ultimo_dia_ano_passado()

    return primeiro_dia_ano_, ultimo_dia_ano