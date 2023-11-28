from random import randint
numero = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print(f'numero sorteado é ', end='')
for n in numero:
    print(f'{n}',end='')
print(f'\nO numero menor é {min(numero)}')
print(f'O numero maior é {max(numero)}')
