somaidade = 0
totalf = 0
maioridadehomem = 0
nomehomemvelho = ''

for p in range(1,5):
    print('_____{} pessoa '.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomemomem = idade
        nomehomemvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemvelho = nome
    if sexo in 'Ff' and idade < 20:
        totalf += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é {} '.format(mediaidade))
print('Neste grupo {} pessoas são mulheres'.format(totalf))
print('A maior Idade de Homem foi {} e se chama {}'.format(maioridadehomem, nome))






