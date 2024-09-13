from datetime import datetime, timedelta
import datetime



def verifica_proxima_ter():

    """
    Essa função é para calcular a data da próxima terça.
    :return: Retorna a data da próxima terça.
    """

    # Obtém a data atual.
    data_atual = datetime.date.today()

    # Obtém o dia da semana atual (0 = segunda-feira, 6 = domingo).
    dia_da_semana_atual = data_atual.weekday()

    # Calcula os dias até a próxima segunda-feira
    dias_ate_proxima_ter = (1 - dia_da_semana_atual + 7) % 7

    # Se hoje é segunda-feira, queremos a próxima segunda-feira, não hoje.
    if dias_ate_proxima_ter == 1:
        dias_ate_proxima_ter = 7

    # Calcula a data da próxima segunda-feira.
    proxima_terca_data = data_atual + datetime.timedelta(days=dias_ate_proxima_ter)

    return proxima_terca_data


def verificar_ter_passada():

    """
    Essa função é para calcular a data da terça passada.
    :return: Retorna a data da terça passada.
    """

    # Obtém a data atual.
    data_atual = datetime.date.today()

    # Obtém o dia da semana atual (0 = segunda-feira, 6 = domingo).
    dia_da_semana_atual = data_atual.weekday()

    # Calcula a diferença de dias até a terça-feira da semana passada.
    # Se hoje é terça-feira ou depois, subtrai (dia_da_semana_atual + 6).
    # Se hoje é antes de terça-feira, subtrai (dia_da_semana_atual + 13).
    if dia_da_semana_atual >= 2:  # Se é terça (1), quarta (2), ..., domingo (6).
        dias_ate_terca_passada = dia_da_semana_atual - 1 + 7
    else:  # Se é segunda (0)
        dias_ate_terca_passada = 6 + dia_da_semana_atual + 1

    # Calcula a data da terça-feira passada.
    terca_passada_data = data_atual - datetime.timedelta(days=dias_ate_terca_passada)

    return terca_passada_data


def obter_primeiro_dia_mes_passado():
    """
    Essa função é para calcular a data do primeiro dia do mês passado.
    :return: Retorna a data do primeiro dia do mês passado.
    """
    # Data atual.
    data_atual = datetime.date.today()

    # Primeiro dia do mês atual.
    primeiro_dia_mes_atual = data_atual.replace(day=1)

    # Primeiro dia do mês passado é o primeiro dia do mês atual menos um mês.
    primeiro_dia_mes_passado = primeiro_dia_mes_atual - timedelta(days=1)
    primeiro_dia_mes_passado = primeiro_dia_mes_passado.replace(day=1)

    return primeiro_dia_mes_passado


def obter_ultimo_dia_mes_passado():
    """
    Essa função é para calcular a data do último dia do mês passado.
    :return: Retorna a data do último do dia do mês passado.
    """
    # Data atual.
    data_atual = datetime.date.today()

    # Primeiro dia do mês atual.
    primeiro_dia_mes_atual = data_atual.replace(day=1)

    # Último dia do mês passado é um dia antes do primeiro dia do mês atual.
    ultimo_dia_mes_passado = primeiro_dia_mes_atual - timedelta(days=1)

    return ultimo_dia_mes_passado


def primeiro_dia_ano_passado():
    """
       Retorna o primeiro dia do ano passado.

       :return: Um objeto datetime representando o primeiro dia do ano passado (somente com mês, dia e ano).
       """
    # Data atual
    data_atual = datetime.date.today()

    # Ano passado
    ano_passado = data_atual.year - 1

    # Primeiro dia do ano passado
    primeiro_dia_ano_passados = datetime.datetime(ano_passado, 1, 1)

    return primeiro_dia_ano_passados.date()


def ultimo_dia_ano_passado():
    """
    Retorna o último dia do ano passado.

    :return: Um objeto datetime representando o último dia do ano passado.
    """
    ano_atual = datetime.date.today()
    ano_passado = ano_atual.year - 1
    ultimo_dia = datetime.datetime(ano_passado, 12, 31)
    return ultimo_dia.date()