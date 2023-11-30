def leiaInt(msg):
       while True:
           try:
            n = int(input(msg))
           except (ValueError,TypeError):
               print('\033[31mERR0: por favor, digite um número inteiro válido.\033[m')
               continue
           except(KeyboardInterrupt):
               print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
               return 0
           else:
               return n
           
def leiaFloat(msg):
       while True:
           try:
            n = float(input(msg))
           except (ValueError,TypeError):
               print('\033[31mERR0: por favor, digite um número inteiro válido.\033[m')
               continue
           except(KeyboardInterrupt):
               print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
               return 0
           else:
               return n
#PROG PRINCIPAL 
n1 = leiaInt('Digite um número inteiro:')
n2 = leiaFloat('Digite um numero real')
print(f'Você digitou o número inteiro {n1}, e o numero real foi {n2}')