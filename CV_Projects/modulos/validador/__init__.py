def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except ( ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro válido.\033[m' )
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m' )
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except ( ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m' )
        else:
            return n