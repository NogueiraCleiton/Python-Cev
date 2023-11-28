'''Crie um programa que gerencia o aproveitamento de um time de futebol.
O progrma vai ler o NOME DO JOGADOR e  QUANTAS PASRTIDAS ELE JOGOU.
Depois vai ler a QUANTIDADE DE GOLS feito em cada partida. No final tudo será guardado em um dicionario,
Incluindo o total de gols feito no campeonato'''
jogador = {}
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Qunatas partidas {jogador["nome"]} jogou ? '))
for c in range (1,tot+1):
    partidas.append(int(input(f'Total de gol na {c}ª partida')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'o campo {k} tem valor {v}.')
print('-='*20)
print(f'O jogador {jogador["nome"]}, jogou {tot} partidas.')
for i,v in enumerate(partidas):
    print(f'   => Na {i+1}ª partida fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')


