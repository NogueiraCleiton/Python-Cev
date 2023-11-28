times = ('gremio','inter','vasco','flamengo','fluminense','palmeiras','sao paulo','curitiba','red bull','sao caetano')
print('=-'*20)
print(times) # classificação
print('=-'*20)
print(f'Os cinto primeiros são{times[0:6]}') # 5 primeiros 
print('=-'*20)
print(f'Os quatro ultimos são:{times[-4:]}')# 4 ultimos
print('=-'*20)
print(f'Times em ordem alfabetica {sorted(times)}') # em oredem 
print('=-'*20)
print(f'O curitiba esta em {times.index("curitiba")+1} posição')