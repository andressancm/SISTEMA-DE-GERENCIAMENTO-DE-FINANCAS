from DATABASE import database

import user
import funcoes_Menu_Despesa
import funcoes_Menu_Poupanca
import funcoes_Menu_Estatisticas
import funcoes_Menu_Renda
from funcoes_Menu_Usuarios import configuracoes_usuario

import pandas as pd

def mostrar_menu_principal(user_id, conn, nome_usuario):

    while True:        

        saldo = user.mostrar_saldo(conn, user_id)
        saldoPoupanca = user.mostrar_saldoPoupanca(conn, user_id)


        print("-----  MENU DE PRINCIPAL  ----")

        print(f"\nSEJA BEM-VINDO, {nome_usuario}!\n")

        print(f"Saldo atual em conta R$: {saldo}")

        print(f" Poupança R$: {saldoPoupanca}")

        print("1. Adicionar renda")

        print("2. Despesa")

        print("3. Extrato")

        print("4. Estatisticas")

        print("5. Poupança")

        print("6. Outros")

        print("7. Configurações do Usuário")

        print("8. Sair")

        escolha = input("Escolha a opção: ")
        conn = database.conectar_banco_de_dados()

        if escolha == '1': 

            funcoes_Menu_Renda.adicionar_renda(user_id, conn)

        elif escolha == '2':

            funcoes_Menu_Despesa.despesa(user_id, conn)

        elif escolha == '3':

            user.exibir_extrato_gastos(user_id, conn)

        elif escolha == '4':
            funcoes_Menu_Estatisticas.estatistica(user_id, conn)
        ######################################
        #elif escolha == '5':
         #   funcoes_Menu_Poupanca()

        #elif escolha == '6':
        ######################################

        elif escolha == '7':
            configuracoes_usuario(user_id, conn)
        
        elif escolha == '8':

            database.desconectar_banco_de_dados(conn)

            break 
        elif escolha == '':
            print("Opção invalida. Tente novamente.")
            continue
        else:

            print("Opção inválida. Tente novamente.")
        
