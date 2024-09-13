import time


def trata_entrada_de_opcao(numero):
    """
    Função de tratamento para caso o usuário digite uma letra ao em vez de número quando for interagir com o Menu.
    :param numero: Essa variável sempre receberá um número do tipo string.
    :return: Sempre retorna um número do tipo string.
    """

    while not numero.isdigit():
        numero = input("Opção inválida, por favor digite novamente: \n")

    return numero


def trata_entrada_de_valor(valor):
    """
        Função de tratamento para caso o usuário digite uma letra ao em vez de um valor quando for interagir com o Menu.
        :param valor: Essa variável sempre receberá um número do tipo string.
        :return: Sempre retorna um número do tipo string.
        """

    while not valor.isdigit():
        valor = input("Valor inválido, por favor digite novamente: \n")

    return valor


def tratamento_de_retorno(parou):

    """
    Essa função com que seja possível o usuário voltar para o menu principal ou encerrar o programa.
    :param parou: É uma variável com um valor booleano.
    :return: Retorna True ou False.
    """

    nova_opcao = input("Digite ""Voltar"" caso queira ir para o menu principal ou qualquer tecla para "
                       "encerrar o programa: ")

    if nova_opcao != "Voltar":
        return not parou
    print("Retornando ao menu principal...")
    time.sleep(3)
    return parou

