
saldo = 0
deposito = 0
Extrato = ''
quantidade_saques = 1
LIMITE_SAQUES = 3

menu = """
    Selecione a Opção desejada !

    [D] Depósito
    [S] Saque
    [E] Extrato
    [0] Sair
"""

print('''
    Bem vindo ao Banco Becks
=========================================      
      ''')

while True:

    print(menu)

    opção = str(input('Digite a opção desejada: ').upper())

    if opção == 'D':

        valor_deposito = float(input('Digite o valor que deseja depositar: R$ '))

        while valor_deposito < 0:
            print('Valor inválido !! Digite novamente uma valor maior que 0.')

            valor_deposito = float(input('Digite o valor que deseja depositar: R$ '))

        saldo += valor_deposito

        Extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
                 
            

        print(f"""
        Depósito de R$ {valor_deposito:.2f} concluído com sucesso !

        Seu saldo agora é de R$ {saldo:.2f}

        """)

    if opção == 'S':

        valor_saque = float(input('Digite o valor que deseja sacar: R$ '))

        if quantidade_saques > LIMITE_SAQUES:

            print('''
                  
    Não foi possível realizar a transação
    Quantidade de saques diários atingida !
                  
                  ''')

        if valor_saque > saldo:

            print('''
                  
    Não foi possível realizar a transação
     Você não possui saldo suficiente !
                  
                  ''')    
        
        elif valor_saque > 0:
        
            saldo -= valor_saque
            quantidade_saques += 1

            print(f"""

    Saque de R$ {valor_saque} realizado com sucesso !
    Seu saldo é de R$ {saldo}

                    """)
            
            Extrato += f'Saque: R$ {valor_saque:.2f}\n'

    if opção == 'E':

        print("\n=============== Extrato ===============")
        print('Não foram realizadas movimentações' if not Extrato else Extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('========================================')


    if opção == '0':
        print('Obrigado ! Volte sempre !')
        break

    #else:
     #   print('Opção Inválida, digite a opção novamente !')