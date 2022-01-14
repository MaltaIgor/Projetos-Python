def leiaInt(numero):
    while True:
        n = str(input(numero))
        if n.isnumeric(): 
            break
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
    return n

#programa principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')