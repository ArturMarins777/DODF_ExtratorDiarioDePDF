import os
import requests
import pandas as pd
import json
from datetime import datetime
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
import schedule
import time

#extratoDiarioDODF.py

def obter_data_atual():
    return datetime.now().strftime('%d-%m-%y')

def baixar_pdf(data, url):
    response = requests.get(url)
    if response.status_code == 200:
        nome_arquivo = f"{data}.pdf"
        with open(nome_arquivo, 'wb') as f:
            f.write(response.content)
        print(f"PDF salvo como {nome_arquivo}")
        return nome_arquivo
    else:
        print("Falha ao baixar o PDF")
        return None

def extrair_paginas_interesse(nome_arquivo):
    with pdfplumber.open(nome_arquivo) as pdf:
        num_paginas = len(pdf.pages)
        pagina_interesse = -1

        for i in range(num_paginas):
            texto_pagina = pdf.pages[i].extract_text()
            if texto_pagina and "ATA DA REUNIÃO DA REDE DISTRITAL DE PROTEÇÃO À MULHER EM" in texto_pagina:
                pagina_interesse = i
                break

    if pagina_interesse != -1:
        reader = PdfReader(nome_arquivo)
        writer = PdfWriter()
        paginas_para_extrair = range(pagina_interesse, min(pagina_interesse + 3, num_paginas))
        for pagina in paginas_para_extrair:
            writer.add_page(reader.pages[pagina])
        
        nome_arquivo_otimizado = nome_arquivo.replace('.pdf', '1.pdf')
        with open(nome_arquivo_otimizado, 'wb') as f:
            writer.write(f)
        print(f"PDF otimizado salvo como {nome_arquivo_otimizado}")
    else:
        print("Texto 'Gerência de contratações' não encontrado no PDF")

def executar_tarefa():
    data_atual = obter_data_atual()
    caminho_arquivo_json = "Caminho/planilha.json"
    
    if not os.path.exists(caminho_arquivo_json):
        print(f"Arquivo {caminho_arquivo_json} não encontrado.")
        return
    
    with open(caminho_arquivo_json, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    
    url = df.loc[df['data'] == data_atual, 'url'].values
    if url.size > 0:
        nome_arquivo = baixar_pdf(data_atual, url[0])
        if nome_arquivo:
            extrair_paginas_interesse(nome_arquivo)
    else:
        print("URL não encontrada para a data atual")

def main():
    schedule.every().monday.at("09:00").do(executar_tarefa)
    schedule.every().tuesday.at("09:00").do(executar_tarefa)
    schedule.every().wednesday.at("09:00").do(executar_tarefa)
    schedule.every().thursday.at("09:00").do(executar_tarefa)
    schedule.every().friday.at("09:00").do(executar_tarefa)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
