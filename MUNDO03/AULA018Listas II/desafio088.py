''' Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
print('=-'*20)
print('JOGO NA MEGA SENA ')
print('=-'*20)
opcoes = int(input('Quantos jogos você quer eu sorteie ?'))
jogo = [[],[],[],[],[],[],[]]
for l in jogo:
    l = randint(0,60)
for c in range(1,opcoes+1):
    print(f'jogo {c}: {jogo}')
