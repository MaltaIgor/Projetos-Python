def fatorial(n, show = False):
    """
    CALCULA A FATORIAL DE UM NUMERO:
    n -> NUMERO
    show = True -> MOSTRA O CALCULO
    """
    f = 1
    while n>0:
        if show:
            print(f'{n}', end='')
            if n>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= n
        n -= 1
    return f



print(fatorial(5, show = True))