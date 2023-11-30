from arquivo import ArquivoExiste
from arquivo import lerArquivo
from arquivo import CriarArquivo
import inter
from inter import cabeçalho
from time import sleep

arq = 'cursoemvídeo.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)
    
while True:
    resposta = inter.menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoas','Sair do Sistema'])
    if resposta == 1:
        #opção de listar o cnteudo de um arquivo 
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('OPC 2')
    elif resposta == 3: 
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)