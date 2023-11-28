'''Crie um programa que leia  NOME , IDADE SEXO de varias PESSOAS. Guardando os dados de cada pessoa em um dicionario e
todos os dicionarios em uma lista. No final mostre: A) Quantas pessoas foram cadastradas B) a média de idade do grupo
C) Uma lista com todas as mulheres D) uma lista com todas as pessoas com idade acima da média'''
pessoas = {}
galera = list()
mulheres = list()
media_idade = 0
while True:
    pessoas['nome'] = str(input('Nome:'))
    while True:
        pessoas['sexo'] = str(input('Sexo M/F')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO ! Digite apenas M/F para sexo !')
    pessoas['idade'] = int(input('Idade:'))
    media_idade += pessoas['idade']
    galera.append(pessoas.copy())
    if pessoas['sexo'] in 'Ff':
        mulheres.append(pessoas.copy())
    conf = str(input('Deseja continuar ? S/N ')).upper()[0]
    if conf in 'Nn':
        break
    
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'A média de idade do grupo é {media_idade/len(galera):.2f}')
print(f'As mulheres cadastradas são {mulheres}')
print('=-'*20)
print('As pessoas com idade acima da média são:')
for p in galera:
    if p['idade'] >= media_idade/len(galera):
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='' )
