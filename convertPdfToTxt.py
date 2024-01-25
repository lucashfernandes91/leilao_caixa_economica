from PyPDF2 import PdfReader
import re
import os.path

"""
    1. Retornar o tamanho do documento
    2. Retirar a primeira página
    3. Retirar as duas ultimas páginas
    4. Ler o documento 
        4.1 Retirar o cabeçalho do documento
    5. Incluir conteudo num arquivo ".txt"
    6. Formatar conteudo do .txt para colocar um lote por linha
"""


pdf_reader = PdfReader("catalogo.pdf")
parts = []


def set_number_of_pages():
    total_pages = len(pdf_reader.pages)
    valid_pages = total_pages - 2
    return valid_pages


def get_number_of_pages():
    return set_number_of_pages()


def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 0 and y < 750:
        parts.append(text)


def txt_save():
    numberOfpages = get_number_of_pages()

    for i in range(1, numberOfpages):
        page = pdf_reader.pages[i]
        page.extract_text(visitor_text=visitor_body)
        text_body = "".join(parts)

    with open("catalogo.txt", mode='a+', encoding='utf-8') as file:
        file.write(text_body + "\n")


def remove_line_break():
    file = open("catalogo.txt", mode="r", encoding="utf-8")

    for line in file.readlines():
        a = line.rstrip('\n')
        with open("catalogo_no_linebreak.txt", mode='a+', encoding='utf-8') as arq:
            arq.write('{}'.format(a))
    file.close()


def txt_format():
    with open('catalogo_no_linebreak.txt', mode='r', encoding='utf-8') as arq:
        result = re.split(r'\d{4}\.\d{6}-\d{1}', arq.readline())

        for item in result:
            with open('saida.txt', mode='a+', encoding='utf-8') as arq:
                arq.write(item + '\n')


def delete_files():
    file_catalog = os.path.isfile('catalogo.txt')
    file_catalog_no_linebreak = os.path.isfile('catalogo_no_linebreak.txt')

    if file_catalog:
        os.remove('catalogo.txt')

    if file_catalog_no_linebreak:
        os.remove('catalogo_no_linebreak.txt')


def convert_to_txt():
    txt_save()
    remove_line_break()
    txt_format()


def start():
    if pdf_reader:
        print('Encontrou o catalogo!')
        convert_to_txt()
        delete_files()

start()
