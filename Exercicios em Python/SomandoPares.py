soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite {}° numero: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print(' A soma dos pares foi {} e corresponde a {} numeros digitados '.format(soma, cont))

