'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
num = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um Numero: '))
    num.append(n)
    if n %2 == 0:
        par.append(n)
    else:
        impar.append(n)
    conf = str(input('Deseja continuar ? [S/N]'))
    if conf in 'Nn':
        break
print(f'Todos os numeros informados são {num}')
print(f'Os numeros pares informados são {par}')
print(f'Os numeros impar infomrados são {impar}')
