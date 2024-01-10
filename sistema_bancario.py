
saldo = 0
deposito = 0
Extrato = ''
quantidade_saques = 0
LIMITE_SAQUES = 3

menu = """

        Bem vindo ao Banco DPS

    Selecione a Opção desejada !

    [D] Depósito
    [S] Saque
    [E] Extrato
    [S] Sair

"""


while True:

    print(menu)

    opção = str(input('Digite a opção desejada: ').upper())

    if opção == 'D':

        valor_deposito = float(input('Digite o valor que deseja depositar: R$ '))
        print('Deposito')

    if opção == 'S':

        print('Saque')


    if opção == 'E':

        print("Extrato")


    if opção == 'S':
        break