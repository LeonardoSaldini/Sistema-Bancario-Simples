
saldo = 0
deposito = 0
Extrato = ''
quantidade_saques = 0
LIMITE_SAQUES = 3

menu = """
=========================================
        Bem vindo ao Banco Becks

    Selecione a Opção desejada !

    [D] Depósito
    [S] Saque
    [E] Extrato
    [0] Sair
=========================================
"""


while True:

    print(menu)

    opção = str(input('Digite a opção desejada: ').upper())

    if opção == 'D':

        valor_deposito = float(input('Digite o valor que deseja depositar: R$ '))

        while valor_deposito < 0:
            print('Valor inválido !! Digite novamente uma valor maior que 0.')

            valor_deposito = float(input('Digite o valor que deseja depositar: R$ '))

        saldo += valor_deposito
                 
            

        print(f"""
        Depósito de R$ {valor_deposito:.2f} concluído com sucesso !

        Seu saldo agora é de R$ {saldo:.2f}

        """)

    if opção == 'S':

        valor_saque = float(input('Digite o valor que deseja sacar: R$ '))
        
        saldo -= valor_saque
        
        quantidade_saques += 1

        if quantidade_saques > LIMITE_SAQUES:

            print('''
                  
    Não foi possível realizar a transação
    Quantidade de saques diários atingida !
                  
                  ''')
            
        
        else:
            print(f"""

    Saque de R$ {valor_saque} realizado com sucesso !

    Seu saldo é de R$ {saldo}

                    """)


    


    if opção == 'E':

        print("Extrato")


    if opção == '0':
        break

    #else:
     #   print('Opção Inválida, digite a opção novamente !')