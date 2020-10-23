print("Palíndromo são frases que são lidas ao inverso e continuam com o mesmo sentido.")

frase = str(input('Digite uma frase: ')).strip().upper()
print('Você digitou a frase: {}'.format(frase))
palavras = frase.split()          # vai separar todas as palavras da frase criando uma lista #
junto = ''.join(palavras)          # vai retirar todos os espaços entre as palavras #
inverso = ''

for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if junto == inverso:
    print('É um palindromo ')
else:
    print('Não é um palindromo')

