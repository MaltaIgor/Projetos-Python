def area(n=1,m=1):
    return n*m


l= float(input('LARGURA (m): '))
c= float(input('COMPRIMENTO (m): '))

a=area(l,c)

print(f'A área de um terreno {l}x{c} é de {a:4.1f} m²')
