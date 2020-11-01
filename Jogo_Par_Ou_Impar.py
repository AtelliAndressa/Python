from random import randint
print('*' * 50)
print(' Jogo do Par ou Impar')
print('*' * 50)
v = 0
while True:
    jogador = int(input('Digite um numero de 0 a 10: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer Par ou Impar? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}, e o total foi {total}')
    print('Deu par' if total % 2 == 0 else "Deu impar")
    if tipo == 'P':
        if total %2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente')
print(f'Game Over! Você venceu {v}')

