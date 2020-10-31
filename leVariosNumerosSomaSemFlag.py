print('Digite vários numeros e mostre a soma sem o flag, a condição de parada é 999')
print('*' *50)
n = contador = soma = 0
n = int(input('Digite um numero: use [999 para parar] '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um numero: use [999 para parar] '))
print('Você digitou {} numeros e a soma entre eles foi {}'.format(contador, soma))