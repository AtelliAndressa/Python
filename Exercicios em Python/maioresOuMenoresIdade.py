from datetime import date

atual = date.today().year
maiortotal = 0
menortotal = 0


for c in range(1,8):
    nascimento = int(input('Digite o {}° ano de nascimento: '.format(c)))
    idade = atual - nascimento
    if idade >= 21:
        maiortotal += 1
    else:
        menortotal += 1
print("Os que são maiores de Idade totalizam {} pessoas".format(maiortotal))
print("Os que são menores de Idade totalizam {} pessoas".format(menortotal))
