import moeda

p = float(input('digite o preço: R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando em 10% o valor é R${moeda.aumentar(p,10)}')