import pandas as pd
import sqlite3
from datetime import datetime

def estatistica(user_id, conn):

    cursor = conn.cursor()
    print("\n-----  MENU DE ESTATÍSTICAS  ----")
    
    # Solicitar ao usuário o mês e o ano desejados
    mes = input("Digite o mês (2 digitos): ")
    ano = input("Digite o ano (4 digitos): ")
    
    # Validar se as entradas de mês e ano são válidas
    while not (mes.isdigit() and ano.isdigit() and 1 <= int(mes) <= 12):
        print("Entrada inválida para mês ou ano. Por favor, tente novamente.")
        mes = input("Digite o mês (2 digitos): ")
        ano = input("Digite o ano (4 digitos): ")

    # Consultar as despesas do usuário para o mês e ano especificados
    cursor.execute('SELECT categoria, valor FROM despesa WHERE user_id = ? AND strftime("%Y-%m", data) = ?', (user_id, f"{ano}-{mes}"))
    dados = cursor.fetchall()

    if dados:

        print("-----  ESTATÍSTICAS  ----")
        print(f"\nMês e Ano selecionados: {mes}/{ano}")

        dados = pd.DataFrame(dados, columns=['Categoria', 'Valor'])

        largura = 50

        max_gasto = dados['Valor'].max()

        for _, linha in dados.iterrows():

            categoria = linha['Categoria']
            gasto = linha['Valor']

            n_barras = int(gasto / max_gasto * largura)

            print(f'{categoria.ljust(15)} | {"#" * n_barras} ({gasto:.2f})')

    else:
        print("Nenhum gasto registrado para o mês/ano especificado.")
