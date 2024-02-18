"""
    1. Abrir arquivo que contém os registros dos lotes
    2. Segregar os campos de cada registro
    3. Registrar os dados no banco

    # Campos para Tabela Lote
        ID = number/unique
        LOTE = number/unique * FALTA
        CONTRATO = number/unique
        DESCRIÇÃO = str
        VALOR

            # Campos futuros
            POSSUI PEDRA
            PESO DO LOTE
            FOTO DO LOTE - img
"""

import re
import sqlite3


def set_contract():
    contract = line.strip()[0:19]
    return contract

def get_contract():
    return set_contract()

def set_price():
    price = re.findall(r'R\$.*', line)
    price = str(price)
    return price[2:-2]

def get_price():
    return set_price()

def lengh_price():
    len_price = len(get_price()) + 1
    return len_price

def set_description():
    price = int(lengh_price())
    description = line[19:-price]
    return description

def get_description():
    return set_description()



with open("saida.txt", mode='r', encoding='utf-8') as file:

    for line in file:
        """print("Contrato: {}".format(get_contract()))
        print("Preço: {}".format(get_price()))
        print("Descrição: {}".format(get_description()))"""

        contract = get_contract()
        description = get_description()
        price = get_price()

        conexao = sqlite3.connect('db-app.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO lote (lote, contrato, descricao, valor) values(?, ?, ?, ?)",
                       ('', contract, description, price))
        conexao.commit()
    conexao.close()
