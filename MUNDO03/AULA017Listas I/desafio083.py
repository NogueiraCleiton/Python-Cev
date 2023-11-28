''' Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
exp = str(input('Digite a expressão:'))
ab = 0
fc = 0 
for c in exp:
    if c == '(':
        ab +=1
    if c == ')':
        fc += 1
print('-='*30) 
if ab == fc:
    print('Expressão válida')
else:
    print('Expressão inválida!')
print(ab)
print(fc)