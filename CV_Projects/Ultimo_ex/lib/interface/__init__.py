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


def linha(tam = 42):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc