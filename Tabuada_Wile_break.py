print('Digite um numero para ver sua tabuada, se desejar parar use um numero negativo')
print('-' * 50)

while True:
    num = int(input("Qual tabuada quer ver:  "))
    if num <0:
        break
    for c in range (1,11):
         print(f'{num} x {c} = {num * c}')
print("Executado com sucesso!")


