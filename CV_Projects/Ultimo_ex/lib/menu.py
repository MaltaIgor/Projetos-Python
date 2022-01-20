
from interface import *

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida.\033[m' )
