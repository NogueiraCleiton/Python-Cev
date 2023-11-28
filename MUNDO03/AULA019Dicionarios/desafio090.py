'''Faça um programa que leia nome e media de um aluno,
guardando tamebm a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela'''
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
if 3<= aluno['media'] <=6:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print(f'O aluno {aluno["nome"]} tem a média {aluno["media"]} e sua situação é {aluno["situação"]}')