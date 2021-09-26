posi=[]
m=0
n=str(input('digite a expressao '))
for v in n:
    if v =='(':
        posi.append('A')
    elif v==')':
        posi.append('F')
if posi.count('A')==posi.count('F'):
    for i, v in enumerate(posi):
        if (i%2==1 and v=='A'):
            m=1
else:
    m=1
if m==1:
    print('função invalida')
else:
    print('função ok')