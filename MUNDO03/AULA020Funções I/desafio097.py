'''Faça um progrma que tenha uma função chamada escreva()
que receba um texto qualquer como parametro e mostre uma mensagem com tamanho 
adaptavel. '''

def escreva(msg):
    tam = len(msg) +4
    print('-'* tam)
    print(f' {msg}')
    print('-'*tam)
#prgrama principa('texto')
escreva('Cleiton Nogueira')
escreva('Curso de python no youtube')
escreva('CeV')