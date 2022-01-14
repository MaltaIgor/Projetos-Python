
def notas(*n, sit=False):
    """
    FUNÇAO QUE ANALISA AS NOTAS E A SITUAÇÃO DE VARIOS ALUNOS
    n: uma ou mais notas dos alunos
    sit: valor opcional, indicando se deve ou nao adicionar a situação
    return: dicionario com varias informações da turma
    """
    turma = {}
    soma = 0
    turma['total']=len(n)
    turma['maior']=max(n)
    turma['menor']=min(n)
    turma['media']= sum(n)/len(n)
    if sit:
        if turma['media'] < 6:
            turma['situacao']='RUIM'
        elif turma['media'] < 8:
            turma['situacao']='BOA'
        else:
            turma['situacao']='EXCELENTE'
    return turma





#programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)