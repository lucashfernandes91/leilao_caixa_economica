from PyPDF2 import PdfReader
import re
import os
import sqlite3

PDF_PATH = "lib/catalogo.pdf"
TXT_PATH = "catalogo.txt"
TXT_NO_BREAK_PATH = "catalogo_no_linebreak.txt"
DB_PATH = "db-app.db"

def get_pdf_reader(pdf_path=PDF_PATH):
	try:
		return PdfReader(pdf_path)
	except Exception as e:
		print(f"Erro ao abrir PDF: {e}")
		return None

def get_valid_page_indices(pdf_reader):
	# Extrai apenas a primeira página
	return [0]

def extract_pdf_text(pdf_reader):
	text = ""
	for i in get_valid_page_indices(pdf_reader):
		page = pdf_reader.pages[i]
		page_text = page.extract_text()
		if page_text:
			text += page_text + "\n"
	return text

def save_txt(text, path=TXT_PATH):
	with open(path, "w", encoding="utf-8") as f:
		f.write(text)

def remove_line_breaks(src=TXT_PATH, dst=TXT_NO_BREAK_PATH):
	with open(src, "r", encoding="utf-8") as fin, open(dst, "w", encoding="utf-8") as fout:
		for line in fin:
			fout.write(line.rstrip("\n"))

def delete_files():
	for path in [TXT_PATH, TXT_NO_BREAK_PATH]:
		if os.path.isfile(path):
			os.remove(path)

def db_exists():
	return os.path.isfile(DB_PATH)

def create_database():
	with sqlite3.connect(DB_PATH) as conn:
		cursor = conn.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS lotes (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			lote TEXT,
			contrato TEXT,
			descricao TEXT,
			valor TEXT,
			peso TEXT,
			Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
		);''')
		conn.commit()

def parse_and_save_to_db(txt_path=TXT_NO_BREAK_PATH):
	pattern_lote = r'(\d{4}\.\d{6}-\d{5}\.\d{3}\.\d{8}-\d{1})'
	with open(txt_path, "r", encoding="utf-8") as f:
		content = f.read()
	result = re.split(pattern_lote, content)

	if not db_exists():
		create_database()

	with sqlite3.connect(DB_PATH) as conn:
		cursor = conn.cursor()
		count = 1
		for section in result:
			if section.strip() == "":
				continue
			if re.match(pattern_lote, section):
				lote = section[:13]
				contrato = section[13:]
				cursor.execute("INSERT INTO lotes (lote, contrato) VALUES (?, ?)", (lote, contrato))
				conn.commit()
			else:
				# Extrai descricao, valor, peso
				descricao = section.strip()
				valor_match = re.search(r'R\$\s*[\d\.]+,\d{2}', section)
				valor = valor_match.group() if valor_match else ""
				peso_match = re.search(r'PESO\s*LOTE:?\s*[\d,]+G', section)
				peso = peso_match.group() if peso_match else ""
				cursor.execute("UPDATE lotes SET descricao=?, valor=?, peso=? WHERE id=?", (descricao, valor, peso, count))
				conn.commit()
				count += 1

def convert_pdf_to_db():
	pdf_reader = get_pdf_reader()
	if not pdf_reader:
		print("PDF não encontrado ou inválido.")
		return
	print("Processando PDF...")
	text = extract_pdf_text(pdf_reader)
	save_txt(text)
	remove_line_breaks()
	parse_and_save_to_db()
	print("Processo concluído. Dados salvos no banco de dados.")

if __name__ == "__main__":
	convert_pdf_to_db()