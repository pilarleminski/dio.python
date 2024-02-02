extrato = []
saldo = 0
conta_saque = 0
limite_saque = 500


while True:
    print()
    print('#### MENU ####')
    print('1 - SAQUE')
    print('2 - EXTRATO')
    print('3 - DEPÓSITO')
    print('4 - SAIR')
    print()
    opcao = int(input('Selecione a opção desejada: '))
    print()

    if opcao == 4:
        print('Saindo...')
        break
        
    elif opcao == 1:
        conta_saque += 1
        if conta_saque > 3:
            print(f'Você atingiu o limite de saque diário.')
            print()
        else:
            saque = float(input('Digite o valor do saque: R$ '))
            if saque > 500:
                print(f'Limite para saque é de R$ {limite_saque}')
                print()
                conta_saque -= 1
            elif saque > saldo:
                print(f'O seu saldo é insuficiente. SALDO R$ {saldo}')
                print()
                conta_saque -= 1
            else:
                saldo -= saque
                extrato.append(saque * -1)
                print('Saque realizado com sucesso')
                print()

    elif opcao == 2:
        print('EXTRATO')
        for valor in extrato:
            print(f"R$ {valor:.2f}")
        print()

    elif opcao == 3:
        if deposito < 0:
            print('Não é possível depositar quantidades negativas.')
        else:
            deposito = float(input('Digite o valor do deposito: R$ '))
            saldo += deposito
            extrato.append(deposito)
            print('Depósito realizado com sucesso')
            print()

    else:
        print('Opção inválida.')
        print()

print('Programa encerrado')

