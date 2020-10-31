print("Gerador de PA")
print('-=' * 10)

termo = int(input('Digite o termo:'))
razao = int(input('Digite a razão: '))
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{} = '.format(termo), end='')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Qauntos termos você quer mostrar a mais? '))
print('P.A. finalizada com {} termos mostrados'.format(total))
