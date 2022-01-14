


def idade(ano):
    """
    FUNÇÃO QUE RETORNA A IDADE BASEADO NO INPUT:
    ANO
    COMPARA COM O ANO ATUAL
    """
    from datetime import datetime
    hoje =  datetime.now().year
    if ano < hoje:
        return hoje - ano
    else:
        return 0


def vota(idade):
    """
    VERIFICA A IDADE DE UMA PESSOA E FALA SE ELA VOTA OU NAO
    """
    if idade < 16:
        return "NÃO VOTA"
    elif idade < 18:
        return "TEM VOTO OPCIONAL"
    elif idade < 65:
        return "TEM VOTO OBRIGATÓRIO"
    else:
        return "TEM VOTO OPCIONAL"





ano = int(input('Em que ano voce nasceu? '))
idade = idade(ano)
vota = vota(idade)

print(f'Você tem {idade} anos e {vota}')