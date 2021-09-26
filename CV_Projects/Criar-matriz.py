matriz=[[0,0,0],[0,0,0],[0,0,0]]
pares=0
soma3=0
maior=0
for n in range(0,3):
    for m in range(0,3):
        matriz[n][m]=(int(input(f'digite o numero para a posição {n,m}')))
        if matriz[n][m]%2==0:
            pares=pares+matriz[n][m]
        if m==2:
            soma3=soma3+matriz[n][m]
        if n==1 and matriz[n][m]>maior:
            maior=matriz[n][m]
for n in range(0,3):
    for m in range(0,3):
        print(f'[{matriz[n][m]:^5}]',end='')
    print()
print(pares,soma3,maior)