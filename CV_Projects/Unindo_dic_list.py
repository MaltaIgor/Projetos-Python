pessoa = dict()
galera = list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa ['idade']
    galera.append(pessoa.copy())
    resp= str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'nN':
        break

print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'A média de idade é {soma/len(galera):5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='' )
