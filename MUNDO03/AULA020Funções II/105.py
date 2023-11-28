'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas
 A maior nota
 A menor nota
 A média da turma
 A situação (opcional)'''
 
def notas(*n, sit= False):
    """_summary_

    Args:
        sit (bool, optional): _description_. Defaults to False.
        param n: uma ou mais notas dos alunos (aceita várias).
        param sit: valor opcional, indicando se deve ou não adicionar a situação.

    Returns:
        _type_: _description_
        r: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r ['Total'] = len(n)
    r ['Maior'] = max(n)
    r ['Menor'] = min(n)
    r ['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = "BOA"
        elif r['Média'] >= 5:
            r['Situação'] = 'REGULAR'
        else:
            r['Média'] = 'Ruim'
    return r 

#PROG PRINCIPAL 
resp = notas(10.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)