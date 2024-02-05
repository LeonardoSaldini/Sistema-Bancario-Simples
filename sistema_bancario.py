import textwrap

print("""
=============================================
            Bem vindo ao     Banco Becks
=============================================
      """)

def menu ():
    menu = """\n
==============================================    
    Selecione a Opção desejada !

    [D] Depositar
    [S] Sacar
    [E] Extrato
    [U] Criar usuário
    [N] Criar nova conta
    [L] Listar contas
    [0] Sair      


"""
    return input(textwrap.dedent(menu).upper()).upper()

def Depositar (valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print("\nDepósito realizado com sucesso !")
    else:
        print("Opeção falhou ! Digite um número válido.")
    return saldo, extrato

def Sacar (saldo, valor, extrato, limite, quantidade_saque, limite_saque):
    excedeu_saque = quantidade_saque >= limite_saque
    excedeu_limite = valor > limite
    sem_saldo = valor > saldo

    if excedeu_saque:
        print("\nNão foi possível realizar o transação\nLimite de saques diários atingidos!")
    elif excedeu_limite:
        print("\t\nNão foi possível realizar o transação\nValor maior que a quantidade diária permitida!")
    elif sem_saldo:
        print("\nNão foi possível realizar a transação\nSem saldo suficiente!")
    else:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        quantidade_saque += 1
        print("\nSaque realizado com sucesso !!!")
    return saldo, extrato, quantidade_saque

def exibir_extrato(saldo, extrato):
    print("\n=============== Extrato ===============")
    print('Não foram realizadas movimentações' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('========================================')

def criar_usuario(usuarios):
    cpf = int(input("Digite o númerodo CPF: "))

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nCpf já cadastrado !")
        return
    
    nome = input("Nome: ")
    data_nascimento = input("Data de nsacimento (dd-mm-aaa): ")
    endereço = input("Digite o endereço (Logradouro, Bairro, Nº e Complemento): ")

    usuarios.append({"Nome": nome, "CPF": cpf, "Data de nascimento": data_nascimento, "Endereço": endereço})

    print("\n\t*** Usuário criado com sucesso ! ***")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")
    return 

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    quantidade_saque = 0
    usuarios = []
    contas = []

    while True:

        opção = menu()

        if opção == 'D':
            valor = float(input("Digite o valor do depósito: R$ "))
            saldo, extrato = Depositar(valor, saldo, extrato)

        elif opção == 'S':

            valor = float(input('Digite o valor que deseja sacar: R$ '))
            saldo, extrato, quantidade_saque = Sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                quantidade_saque=quantidade_saque,
                limite_saque=LIMITE_SAQUES 
            )

        elif opção == 'E':
            exibir_extrato(saldo, extrato)

        elif opção == 'U':
            criar_usuario(usuarios)

        elif opção == 'N':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opção == 'L':
            listar_contas(contas)

        elif opção == '0':
            print('Obrigado ! Volte sempre !')
            break

        else:
            print("@@@ Operação inválida, digite a opção novamente. @@@")

main()

