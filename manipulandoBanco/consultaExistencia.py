from conexaoBanco import cursor


def consulta_existencia_de_data(data_referencial):
    consulta_data = """
            SELECT * FROM lucro_diario where data_dia = %s;

            """
    cursor.execute(consulta_data, (data_referencial,))
    resultado = cursor.fetchone()
    return resultado
