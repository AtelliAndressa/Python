print('Os numeros primos são aqueles que são apenas divisíveis por eles mesmo e pelo número 1')

num = int(input('Digite um numero para saber se é primo: '))
total = 0

for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')    # coloca o resultado em amarelo #
        total += 1                      # conta quantos foram divisíveis #

    else:
        print('\033[m', end=' ')        # retorna para cor padrão #
    print('{}'.format(c), end=' ')      # vai escrever todos os numeros até chegar no destino #
print('\n O numero foi divisivel {} vezes'.format(total))
if total == 2:
    print(' É um número primo!')
else:
    print(' Não é um número primo.')