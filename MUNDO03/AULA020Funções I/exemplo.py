
#ROTINA
def lin():
    print('-=-'*30)
lin()
print('CURSO EM VIDEO')
lin()
print('APRENDA PYTHON')
lin()
print('CURSO EM VIDEO')
lin()
'''
--------------------------------------------------------------
def soma(a, b):
    s = a + b
    print(s)
------------------------------- DEIXAR DUAS LINHAS 
-------------------------------ENTRE DEF E PROG PRINCIPAL 
soma(2,3)
soma(6,3)
---------------------------------------------------------------

def soma(a, b):
    print(f' A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
#------------------------------- DEIXAR DUAS LINHAS 
#-------------------------------ENTRE DEF E PROG PRINCIPAL 
soma(2,3)
soma(6,3)
----------------------------------------------------------------
def contador(*núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')


contador(2,1,7)
contador(8,0)
contador(2,5,6,1,8,)


def contador(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm}  e são ao todo {tam} numeros')
    

contador(2,1,7)
contador(8,0)
contador(2,5,6,1,8,)
'''