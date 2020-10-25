n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opção = 0

while opção != 5:
    print('''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa ''')
    opção = int(input('Qual é a sua opção: '))
    if opção == 1:
        print('O valor da soma é {} '.format(n1 + n2))
    elif opção == 2:
        print('O valor da multiplicação é {} '.format(n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('O maior numero é {} '.format(n1))
        else:
            n2 > n1
            print('O maior numero é {} '.format(n2))
    elif opção == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opção == 5:
        print('Ate breve.')
print("Fim do programa")
