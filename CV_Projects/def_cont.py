from time import sleep

def contador(i,f,p):
    print(f'Contagem de {i} ate {f} de {p} em {p}.')
    cont = i
    if i<f:
        while cont<=f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
    else:
        while cont>=f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p   

contador(1,10,1)
print()
contador(10,1,-1)

while True:
    i = int(input('Qual o início? '))
    f = int(input('Qual o fim? '))
    p = int(input('Qual o passo? '))
    if f>i and p>0:
        break
    elif i>f and p<0:
        break
    else:
        print('As entradas não fazem sentido')
contador(i,f,p)