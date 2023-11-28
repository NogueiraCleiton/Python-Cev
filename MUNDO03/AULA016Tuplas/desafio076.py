listagem = ('Lápis', '1.75',
            'Borracha','2.00',
            'caderno','15.00',
            'Estojo','25.00')
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40} ') # CENTRALIZADO ENTRE 40 CARACTERES
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}', end='')
    else:
        print(f"R${listagem[pos]}")
print('-'*40)