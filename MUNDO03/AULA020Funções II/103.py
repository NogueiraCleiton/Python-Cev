'''Função chamada ficha() recebe dois parametros
NOME/GOL. devera mostras a ficha mesmo sem dados completos'''

def ficha (jog ='<Desconhecido>' , gol = 0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato !')
# PROG PRINCIPAL
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0 
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)
    