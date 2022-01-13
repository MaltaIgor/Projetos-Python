def maior(lista):
    lista.sort()
    return lista[len(lista)-1]

lista = []
while True:
    numero = int(input(f'Numero {len(lista)+1}: '))
    lista.append(numero)
    res = str(input('Quer continuar? [S/N' )).upper()[0]
    if res in 'N':
        break
print(maior(lista))