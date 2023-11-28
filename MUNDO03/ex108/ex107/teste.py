''' Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
import moeda

preco = float(input('Digite o valor R$:'))
print(f'A metade de {moeda.moeda(preco)} é {moedas.metade(preco)}')
'''print(f'O dobro de {preco} é {moedas.dobro(preco)}')
print(f'Aumentando 10% temos R${moedas.aumento(preco, 10)}')
print(f'Diminuindo 7% temos R${moedas.diminuir(preco, 7)}')'''
5