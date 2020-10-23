print('10 Termos de uma PA')

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razao: '))
decimotermo = termo + (10-1) * razao

for c in range(termo,decimotermo,razao):
    print(c)