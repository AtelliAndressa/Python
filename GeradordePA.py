print("Gerador de PA")
print('-=' * 10)

termo = int(input('Digite o termo:'))
razao = int(input('Digite a razão: '))
contador = 1

while contador <= 10:
    print('{} = '.format(termo), end='')
    termo += razao
    contador += 1