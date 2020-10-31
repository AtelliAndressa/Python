print('Sequencia de Fibonacci')
print('-=' * 10)
n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
print('Os termos são {} = {}'.format(t1,t2), end='')
contador = 3
while contador <= n:
    t3 = t1 + t2
    print(' = {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print('= Fim')