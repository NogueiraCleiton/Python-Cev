num = (int(input('Digite um valor: ')),
       int(input('Digite um mais um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite o ultimo valor: ')))
print(f'Voce digitou os numeros {num}')
print(f'O numero 9 apareceu {num.count(9)} veses') # Qunatas veses apareceu o numero nove 
if 3 in num:
    print(f'O numero 3 foi digitado na {num.index(3)+1}ª posição ')# posição do numero 3 
else:
    print('O numero 3 não foi digitado nehuma vez')
print('os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')