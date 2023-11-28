'''Crie um programa que tenha a função chamada fatorial() que receba dois parâmetros: 
o 1 é um numero  a calcular 
o 2 é uma outro chamado show, que será um valor lógico(opcional)indicando se sera mostrado ou não
na tela o processo de calculo de fatorial '''
from math import factorial
def fatorial(n, show=False):
    """
    -> calcula o fatorial de um numero 
    param n: numero para calculo de fatorial
    param show: (opcional) Mostrar conta 
    return: 0 valor de fatorial de um n.
    """
    s = factorial(n)
    if show == True:
        n2 = n
        global f
        f = 1
        c = n
        for n in range(n,0,-1):
            print(n, end='')
            print(' x ' if n>1 else ' = ', end='')
            f *= c
            c -= 1
        print(s)
    
    else:
        print(factorial(n))



#fatorial(5)
help(fatorial)