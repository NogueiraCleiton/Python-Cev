'''Faça um programa que tenha uma função chamda area(), que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a area do terreno '''
def area(l,c):
    a = l*c
    print(f'A área de um terreno de {l}x{c} é de {a}m².')      
    

print('CONTROLE DE TERRENOS')
print('-='*10)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m)'))
area(l, c)