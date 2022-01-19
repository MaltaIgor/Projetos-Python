def aumentar(preço, taxa, format = False):
    res = preço + (preço * taxa/100)
    return res if format is False else moeda(res)

def diminuir(preço, taxa, format = False):

    res = preço - (preço * taxa/100)
    return res if format is False else moeda(res)

def dobro(preço, format = False):

    res = preço * 2
    return res if format is False else moeda(res)

def metade(preço, format = False):

    res = preço / 2
    return res if format is False else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:8.2f}'.replace('.',',')


def resumo(preço=0,aum=10,dim=10):
    print(f'-'* 30)
    print('RESUMO DO VALOR'.center(30))
    print(f'-'* 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Aumentando o preço: \t{aumentar(preço, aum, True)}')
    print(f'Diminuindo o preço: \t{diminuir(preço, dim, True)}')
    print(f'-'* 30)