'''Aprimore o desafio 093 para qeu ele funcione com varios jogadores, 
incluindo um sistema de visualização de detalhamento
do aproveitamento de cada jogador'''
total_gols  = {}
total_gols['nome'] = str(input('Nome do jogador: '))
gols = []
total_gols['gols'] = gols
total_gols['total']= 0

partidas = int(input(f'Quantas partidas {total_gols["nome"]} jogou? '))
for c in range (0,partidas):
    gols.append(int(input(f'Quantos gols na {c+1} partida')))
for v in gols:
    total_gols['total'] += v
print('-=-'*40)
print(total_gols)
print('-=-'*40)
for k,v in total_gols.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*40)
print(f'O jogador {total_gols["nome"]} jogou {partidas} partidas.')
print('-=-'*40)
print(f'{'Cod.Nome':>5}',f'{'Gols':>15}',f'{'Total':>15}')