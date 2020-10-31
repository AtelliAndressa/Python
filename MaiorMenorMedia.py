resp = 'S'
soma = contador = media = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    contador += 1
    if contador ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / contador
print('Você digitou {} numeros e a média foi {} '.format(contador, media))
print('Maior numero foi {}  e  o menor numero foi {}'.format(maior, menor))