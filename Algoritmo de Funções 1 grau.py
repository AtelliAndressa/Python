print('-=' *10)
print(f'Função de 1° Grau')
print('-=' * 10)

fixo = float(input('Qual o valor do salario fixo ganho mensalmente?: R$  '))
vendas= float(input('Qual o valor total das vendas que você vendeu este mês?: R$  '))
comissão = float(input('Qual o percentual de comissão ganho sobre as vendas? '))
total = 0
if vendas >= 200000:
    total = (vendas * (comissão + 0.5)/100) + fixo
else:
    total = ((vendas * comissão)/100) + fixo
print(f'O total de seu salario recebido foi R$ {total:.2f} neste mês')

# Exemplo percentual ganho 1% abaixo de 200.000,00 de vendas
# b = fixo
# a = vendas
# y = total (salário)
# total = 0.01*vendas + fixo
# y = 0.01x + b

# Exemplo percentual ganho 1% + 0.5% acima de 200.000,00 de vendas
# total = 0.015*vendas + fixo
# y = 0.015x + b
#Espero que tenha entendido corretamente o proposto
#fique com Deus prof!!!