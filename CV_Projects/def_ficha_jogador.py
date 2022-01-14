def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols.')





j = str(input('Qual o nome do jogado? '))
g = str(input('Quantos gols ele marcou? '))
if g.isnumeric():
    g= int(g)
else:
    g=0
if j.strip() == '':
    ficha(gol=g)
else:
    ficha(j, g)