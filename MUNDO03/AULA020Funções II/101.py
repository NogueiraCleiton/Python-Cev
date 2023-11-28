'''Crie uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando uma valor literal indicando se uma pessoa tem voto opcional negado ou obrigatorio nas eleições'''
from datetime import date
def voto(i=0):
    ano = date.today().year
    voto = ano - i 
    if voto < 16:
        res = 'Não vota'
        print(f'Você tem {voto} anos e você {res}') 
    if voto <18 and voto > 16 or voto > 65:
        res = 'opcional'
        print(f'Você tem {voto} anos e seu voto é {res}') 
    if voto > 18 and voto < 60:
        res = 'obrigatorio'
        print(f'Você tem {voto} anos e seu voto é {res}') 


i = int(input('Ano de nascimento:')) 
voto(i)