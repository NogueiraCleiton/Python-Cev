import inter
from inter import cabeçalho
from time import sleep

while True:
    resposta = inter.menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoas','Sair do Sistema'])
    if resposta == 1:
        cabeçalho('OPC 01')
    elif resposta == 2:
        cabeçalho('OPC 2')
    elif resposta == 3: 
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)