# coding=UTF-8

import re
import csv

files = ['ouro', 'diamante']

def lot_filter(item):
    result_list = []
    list_of_words = [
            'BAIXO'
            ,'massa,'
            ,'massa;'
            ,'PLATINA,', 'PLATINA;'
            ,'PRATA', 'PRATA,', 'PRATA;'
            ,'PEDRA', 'PEDRA,', 'PEDRA;'
            ,'PEDRAS', 'PEDRAS,', 'PEDRAS;'
            ,'pedra', 'pedra,', 'pedra;'
            ,'pedras', 'pedras,', 'pedras;'
            ,'16k', '12k'
            ,'enchimento', 'enchimento,', 'enchimento;', 'enchimento(s),', 'madrepérola,', 'madrepérola;'
            ,'pérola', 'pérola,', 'pérola;'
        ]

    for word in list_of_words:   
        find = item.find(word)
        result_list.append(find)

    for analysis in result_list:
        if analysis != -1:
            return True                   
    return False
        
def lot_amount(item):
    find = str(re.findall(r'\d{0,3}.?\d{1,3},00.$', item))
    amout = find[2:]
    amout = amout[:-2]
    return amout

def lot_description(item):
    description = item[27:]
    return description

def lot_weight(item):
    weight = re.search(r'\d{1,3}\,\d{2}', item).group()
    return weight

def read_txt():
    arq = open(text_file, encoding="utf8")
    content = arq.readlines()
    return content

def save_planilha():
    content = read_txt()

    with open(spreadsheet, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['LOTE', 'VALOR', 'PESO', 'DESCRICAO']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()

        for item in content:   
            if lot_filter(item) == False:
                lot = item[:7]
                amount = lot_amount(item)
                weight = lot_weight(item)
                description = lot_description(item)
                writer.writerow({'LOTE': lot, 'VALOR': amount, 'PESO': weight, 'DESCRICAO': description})
                #print('{} - Valor: {}, Peso: {}, Descrição: {}'.format(lote, valor, peso, descricao))
            
for file in files:
    text_file = file +'.txt' 
    spreadsheet = file +'.csv' 
    save_planilha()