"""
    1. Abrir arquivo que contém os registros dos lotes
    2. Segregar os campos de cada registro
    3. Registrar os dados no banco

    # Campos para Tabela Lotes (ID, LOTE, CONTRATO, DESCRIÇÃO, VALOR)
        # Campos futuros
        POSSUI PEDRA
        PESO DO LOTE
        FOTO DO LOTE - img
"""

import re
import sqlite3

def set_lote():
    lote = line.strip()[0:13]
    return lote

def get_lote():
    return set_lote()

def set_contract():
    contract = line.strip()[13:32]
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
    description = line[32:-price]
    return description

def get_description():
    return set_description()


with open("saida.txt", mode='r', encoding='utf-8') as file:
    conexao = sqlite3.connect('db-app.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE lotes (
                     id        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     lote      TEXT    NOT NULL,
                     contrato  TEXT    NOT NULL,
                     descricao TEXT    NOT NULL,
                     valor     TEXT    NOT NULL,
                     Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);
                      ''')

    for line in file:
        lote = get_lote()
        contract = get_contract()
        description = get_description()
        price = get_price()

        cursor.execute("INSERT INTO lotes (lote, contrato, descricao, valor) values(?, ?, ?, ?)",
                       (lote, contract, description, price))
        conexao.commit()
    conexao.close()