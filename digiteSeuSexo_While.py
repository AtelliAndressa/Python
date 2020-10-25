
sexo = str(input("Informe seu sexo [F/M]: " )).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input("Dados inválidos. Por favor, digite novamente: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso. ".format(sexo))