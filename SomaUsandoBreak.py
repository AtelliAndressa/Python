num = contador = soma = 0
while True:
    num = int(input("Dig um numero: [Para parar use 999] "))
    if num == 999:
        break
    soma += num
    contador += 1

print(f'Você digitou {contador} numeros e a soma é {soma}')
