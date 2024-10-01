# DODF_ExtratorDiarioDePDF

Este projeto extrai automaticamente as páginas de interesse do Diário Oficial do Distrito Federal (DODF), com base em uma busca específica dentro dos arquivos PDF publicados. O script baixa o arquivo PDF do DODF para o dia atual e extrai até 3 páginas começando a partir da página onde o termo de busca é encontrado.
## Funcionalidades

- Baixa automaticamente o PDF do DODF para o dia atual.
- Busca por um termo específico no conteúdo do PDF.
- Extrai até 3 páginas a partir da página onde o termo de busca é encontrado, podendo ser alterado na linha 43.
- Salva um novo PDF contendo as páginas de interesse.
- Programado para rodar diariamente de segunda a sexta-feira às 9:00h.

## Requisitos 🔧

- Python 3.x
- Bibliotecas necessárias (instaláveis via `pip`):
  - `requests` (https://pypi.org/project/requests/)
  - `pandas` (https://pypi.org/project/pandas/)
  - `pdfplumber` (https://pypi.org/project/pdfplumber/)
  - `PyPDF2` (https://pypi.org/project/PyPDF2/)
  - `schedule` (https://pypi.org/project/pikepdf/)
  - `pikepdf` (https://pypi.org/project/schedule/)

### Instalação ⚙️

1. Clone este repositório:
   ```bash
   git clone https://github.com/ArturMarins777/DODF_ExtratorDiarioDePDF.git

2. Navegue até o diretório do projeto:
   ```bash
   cd DODF_ExtratorDiarioDePDF

3. Instale as dependências:
   ```bash
   pip install requests pandas pdfplumber PyPDF2 schedule
   pip install -r requirements.txt

## Personalização

### Termo de Busca

Por padrão, o script procura pelo termo **"Gerência de contratações"** nos PDFs. Caso queira alterar o termo, siga os seguintes passos:

1. No arquivo `extratoDiarioDODF.py`, localize a função `extrair_paginas_interesse`.
2. Substitua o termo `"Gerência de contratações"` pelo termo que deseja procurar.

    Exemplo:

    ```python
    if texto_pagina and "Novo Termo de Busca" in texto_pagina:
    ```

### Alteração do Número de Páginas Extraídas

O script, por padrão, extrai até 3 páginas a partir da página onde o termo de busca é encontrado. Para modificar essa quantidade:

1. No arquivo `extratoDiarioDODF.py`, localize a linha na função `extrair_paginas_interesse`:

    ```python
    paginas_para_extrair = range(pagina_interesse, min(pagina_interesse + N, num_paginas))
    ```

2. Substitua `N` pelo número de páginas que deseja extrair.

### Agendamento 🛠️

O script está configurado para rodar automaticamente em dias úteis às 9:00h. Se você quiser mudar o horário ou os dias da semana:

1. No arquivo `extratoDiarioDODF.py`, localize a função `main`.
2. Modifique as linhas de agendamento conforme necessário. Exemplo:

    ```python
    schedule.every().monday.at("09:00").do(executar_tarefa)
    ```

Você pode alterar o horário ou adicionar/remover dias de acordo com suas preferências.

## Contribuição 🤝

Contribuições são bem-vindas! Sinta-se à vontade para:

- Abrir um Pull Request com melhorias e correções.
- Relatar problemas e sugerir novos recursos na aba de [Issues](https://github.com/DODF_ExtratorDiarioDePDF/issues).
- Além disso, adoraria me conectar com outros profissionais e entusiastas da tecnologia! Sinta-se à vontade para me adicionar no [LinkedIn](https://www.linkedin.com/in/arturmarins/) para trocarmos ideias e compartilharmos conhecimento.
-Este é meu primeiro projeto disponibilizado aqui, então toda ajuda é bem-vinda.

## Licença 📜

Este projeto está licenciado sob a [MIT License](LICENSE).

