'''faça um programa que tenha uma função chamada contador()
que receba 3 parâmetros: inicio, fim e passo e raliza a contagem 
A) de 1 até 10, de 1 em 1 
B) de 10 até 0, de 2 em 2
C) Uma contagem personalizada'''
from time import sleep
def cont(i,f,p):
    if p <0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'A contagem de {i} até {f} de {p} em {p} é:')
    sleep(2.5)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='',flush=True)
            sleep(0.5)
            cont += p
        print('FIM !')
    else:
        cont = i 
        while cont>= f:
            print(f'{cont} ', end='',flush=True)
            sleep(0.5)
            cont-= p
    print('FIM')
cont(1,10,1)
cont(10,0,2)
print('-='*20)
print('Agora é sia vez de personalizar a contagem ! ')
ini = int(input('Início: '))
fim = int(input('Fim'))
pas = int(input('Passo: '))
cont(ini,fim,pas)
