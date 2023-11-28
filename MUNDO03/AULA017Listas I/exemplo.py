'''LISTAS ESTÃO ENTRE ()
LISTAS PODEM SER MUTAVEIS COM O COMANDO LANCHE[3]=PICOLE 
PARA ADICIONAR ELEMENTOS NOVOS NA FINAL DA LISTA LANCHE.APPEND('COOKIE')
PARA ADICIONAR ELEMENTOS EM QUALQUER POSIÇÃO LANCHE.INSERT(0,'CACHORRO QUENTE') ALTERA AS POSIÇÕES PRA FRENTE = adiconado na posição 0 
PARA APAGAR ELEMENTOS DA LISTA 
DEL.LANCHE[3] SELECIONA O ELEMENTO
LANCHE.POP(3) NORMALMENTE PARA ELIMINAR O ULTIMO ELEMENTO se estive vazio

for c, v in enumerate(valores):
    PRINT (PARA A POSIÇÃO (C) ENCONTREI O VALOR (V))

if 'pizza' in lanche: VERIFICA SE ESTA NA LISTA
LANCHE.REMOVE('PIZZA') TEM QUE INFORMAR O VALOR A SER REMOVIDO

CRIAR LISTAS:
valores=lisT(range(0,10))
valores.sort() coloca a lista em ordem 
valores.sort(reverse=True) coloca a lista em ordem reversa
LEN(VALORES) TAMANHO DA LISTA EM ELEMENTOS.
valores.insert(2,0) inerio valor na (posição,valor inserido)
 

VALORES.SORTE() ORDENA OS VALORES DA LISTA
VALORE.SORTE(REVERSE=TRUE) ORDENA OS VALORES DE TRAZ PRA FRENTE
  
a = [2,3,4,5,]
b = a 

elas ficam ligadas diretamente

a = [2,3,4,5,]
b = a [:]
recebe uma copia de A porem alterando separadamente, sem ligação direta '''

valores= list()
for x in range (0,5):
    valores.append(int(input('Digite um valor')))
for c,x in enumerate(valores):
    print(f'na posição {c} temos o valor {x}!')
print('Chegamos ao final da lista ')