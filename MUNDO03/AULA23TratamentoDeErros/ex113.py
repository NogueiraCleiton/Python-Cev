def leiaInt(msg):
       while True:
           try:
                n = int(input(msg))
           except (ValueError,TypeError):
               print('ERR0: por favor, digite um número inteiro válido.')
               continue
           else:
               re
           
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um úmero inteiro válido.\033[m')
        if ok: 
            break
    return valor  
try:
    
nI = int(input('Digite um inteiro:'))
nR = float(input('Digite um Real:'))

#PROG PRINCIPAL 
n = leiaInt('Digite um número:')
print(f'Você digitou o número {n}')