'''Crie um progrma que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO
e cadastre-os (com idade) em um dicionario se por acaso a CTPS for diferente de ZERO,
o dicionario recebera tamebem o ano de contratação e salário.
Calcule e acresente, além da idade, com quantos anos a pessoa vai se APOSENTAR'''
from datetime import date
ano = date.today().year
inss = {}
inss['nome']=str(input('Digite seu nome:'))
inss['nasc']=int(input('Ano de nascimento: '))
inss['CTPS']=int(input('Nº Carteira de trabalho (0 se não tem):'))
if inss['CTPS'] != 0:
    inss['Ano de contratação']= int(input('Ano de contratação:'))
    inss['Aposentadoria'] = (inss['Ano de contratação']- inss['nasc'])+35
    inss['salario']=int(input('Salário: R$'))
    print('=-'*30)
    for k,v in inss.items():
        print(f'   -{k} tem o valor {v}')
else:
    print('=-'*30)
    for k,v in inss.items():
        print(f'   -{k} tem o valor {v}')