'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

t_pessoas = 0
dado = list()
maior_peso = []
menor_peso = []
while True:
    dado.append(input("digite seu nome: "))
    dado.append(input("digite seu peso: "))
    if dado[1] == '70':
        menor_peso.append(dado[0])
    if dado[1] == '100':
        maior_peso.append(dado[0])
    t_pessoas += 1
    dado.clear() 
    conf = int(input('Deseja continuar ? [1-S\ 2-N]'))    
    if conf != 1:
        break 
print(f'Tivemos um total de {t_pessoas} pessoas cadastradas')
print(f'{menor_peso} tem 70 kg')
print(f'{maior_peso} tem 100 kg')
