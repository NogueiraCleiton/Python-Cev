def LeiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f'\033[0;31mERRO: \"{entrada}\ é um preço inválido! \033[m"')
        else:
            válido = True
            return float(entrada)