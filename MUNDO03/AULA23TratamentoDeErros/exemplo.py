try: #   operação 
    a = int(input('Numerador'))
    b = int(input('denominador'))
    r = a/b 
except (TypeError, ValueError):
    print(f'Tivemos im pronlema com os tipos de dados infomrados')
    
except ZeroDivisionError:
    print('Não é possível divid um numero por zero')
    
except KeyboardInterrupt:
    print('O usuario preferiu não infomrar os dados!')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempr, muito obrigado!')