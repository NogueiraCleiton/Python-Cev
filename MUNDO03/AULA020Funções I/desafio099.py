''' faça um programa que tenha uma função chamada maior(), que
receba varios parametros com valores inteiros.

seu programa tem que analisar todos os valores e dizer qual deles é maoir '''
from time import sleep
def maior(*núm):
    cont = maior = 0 
    print('\n Analisando os valores passados')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores no total.')
    print(f'O maior valor informado foi {maior}.')


#programa principal 
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()