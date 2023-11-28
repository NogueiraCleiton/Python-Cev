''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
val = []
maior = menor = 0
for c in range (0,5):
    val.append(int(input('Digite um valor :')))
    if c == 0:
        maior = menor = val[0] 
    else:
        if val[c] > maior:
            maior = val[c]
        if val[c] < menor:
            menor = val[c]
print(f'Você digitou os valores {val}')
print(f'O maior valor difgitado foi {maior} nas posições ', end='')
for i,v in enumerate(val):
    if v == maior:
        print(f'{i}...',end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i,v in enumerate(val):
    if v == menor:
        print(f'{i}...',end='')
print()