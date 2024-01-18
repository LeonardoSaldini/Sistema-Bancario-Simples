
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
            print('\nValor inválido !! Digite novamente uma valor maior que 0.')

            valor_deposito = float(input('Digite o valor que deseja depositar: R$ '))

        saldo += valor_deposito
        Extrato += f'Depósito: R$ {valor_deposito:.2f}\n'       

        print(f"\nDepósito de R$ {valor_deposito:.2f} concluído com sucesso !")


    if opção == 'S':

        valor_saque = float(input('Digite o valor que deseja sacar: R$ '))

        if quantidade_saques > LIMITE_SAQUES:

            print('\nNão foi possível realizar a transação\nQuantidade de saques diários atingida !')

        elif valor_saque > saldo:

            print('\nNão foi possível realizar a transação\nVocê não possui saldo suficiente !')    
        
        else: #valor_saque > 0:
        
            saldo -= valor_saque
            quantidade_saques += 1

            print(f"\nSaque de R$ {valor_saque} realizado com sucesso !")
            
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
    #    print('Opção Inválida, digite a opção novamente !')