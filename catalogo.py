# coding=UTF-8
import re

content = ''
count = 0

result = re.split(r'0453\.0', content)

for item in result:
    diamante = item.find('diamante')
    pedra = item.find('pedra')

    if pedra != -1:
        count = count + 1
        arquivo = 'pedra.txt'
    elif diamante != -1:
        count = count + 1
        arquivo ='diamante.txt'
    else:
        count = count + 1
        arquivo = 'ouro.txt'

    with open(arquivo, mode='a+', encoding='utf-8') as arq:
        arq.write(item + '\n')

    print(str(count) + '. ' + item)