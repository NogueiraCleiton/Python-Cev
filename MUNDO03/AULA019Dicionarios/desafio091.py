'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
Guarde esses resulatdos em um dicionarios. No final, coloque esses dicionarios em ordem, 
sabendo que o vencedor tirou o maior numero no dado. 
'''
from random import randint
from operator import itemgetter
from time import sleep
lista = {'jogador 1':randint(1,6),
         'jogador 2':randint(1,6),
         'jogador 3':randint(1,6),
         'jogador 4':randint(1,6)}
ranking = ()
print('Valores sorteados:')
for k,v in lista.items():
    print(f' o {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(lista.items(), key=itemgetter(1), reverse=True)
print('-=-'*30)
print('  === RANKING DOS JOGADORES ===')
for i,v in enumerate(ranking):
    print(f'O {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)