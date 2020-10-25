from random import randint

computador = randint(0,10)
print('Descubra o numero que estou pensando de 0 a 10. ')
print('tente adivinhar: ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite um número: '))
    palpite += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("mais....Tente mais uma vez.")
        elif jogador > computador:
            print("menos....Tente mais uma vez.")
print("Você adivinhou! O numero que eu pensei e que você digitou foi {}, com {} tentativas".format(jogador, palpite))

