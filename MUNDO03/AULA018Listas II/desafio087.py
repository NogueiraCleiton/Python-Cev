'''Aprimore o desafio anterior, mostrando no final
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = list()
some = 0
soma3c = 0
mseg = 0
for c in range(0,3):
    matriz.append(int(input(f'Digite um valor para [0,{c}]: ')))
for c in range(0,3): 
    matriz.append(int(input(f'Digite um valor para [1,{c}]: '))) 
for c in range(0,3):
    matriz.append(int(input(f'Digite um valor para [2,{c}]: ')))        
print(f'[{matriz[0]}]',f'[{matriz[1]}]',f'[{matriz[2]}]')
print(f'[{matriz[3]}]',f'[{matriz[4]}]',f'[{matriz[5]}]')
print(f'[{matriz[6]}]',f'[{matriz[7]}]',f'[{matriz[8]}]')
for c,v in enumerate (matriz):
    some += v
print(some)
for c,v in enumerate (matriz[3:6]):
    soma3c += v
print(soma3c)
for c,v in enumerate (matriz[6:9]):
    if v > mseg:
        mseg = v
print(mseg)