import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/NogueiraNoob')
except urllib.error.URLError:
    print('O perfil de Cleiton no GitHib não está disponivel no momento')
else:
    print('Tudo OK')
    print(site.read())