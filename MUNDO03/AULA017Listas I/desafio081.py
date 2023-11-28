'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
num = []
c = 0
while True:
   num.append(int(input('Digite um numero: ')))
   c += 1
   r = str(input('Deseja continuar ? [S/N]'))
   if r in 'Nn':
        break
print('=-'*30)
print(num)
print(f'Você digitou um total de {c} numeros !')
num.sort(reverse=True)
print(f'Os numeros em ordem decresente são {num}...')
if 5 in num:
    print('O valor 5 ESTÁ na lista!')
else:
    print('O valor 5 NÃO está na lista!')