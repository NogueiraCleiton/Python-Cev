palavra = ('APRENDER','PROGRMAR','LINGUAGEM','PYTHON',
            'CURSO','GRATSI','ESTUDAR','PRARICAR','TRABALHAR',
            'MERCADO','PROGRAMADOR','FUTURO')
for n in palavra:
    print(f'\n Na palavra {n} temos ', end='')
    for letra in n:
        if letra.lower() in 'aeiou':        
            print(letra, end=' ')