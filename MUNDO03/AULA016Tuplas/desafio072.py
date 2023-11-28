num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
       'doze','treze','catorze','quinze','dezesesi','dezesete','dezoito','dezenove','vinte')  
while True:
    n = int(input('Digite um numero entre 0-20:'))
    if n >= 0 and n <=20:
      print(f'voce escolheu o numero {num[n]}') 
      break
    else:
        n = int(input('Numero invalido. Digite um numero entre 0-20: '))
