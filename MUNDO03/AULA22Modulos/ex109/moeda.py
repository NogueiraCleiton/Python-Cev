def aumento(preco = 0, taxa = 0, formato=False):
    """_summary_

    Args:
        preco (int, optional): _description_. Defaults to 0.
        taxa (int, optional): _description_. Defaults to 0.
        formato (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0, taxa = 0, formato=False):
    res =  preco - (preco * taxa/100 )
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato=False):
    res = preco*2
    return res if formato is False else moeda(res)

def metade(preco = 0, formato=False):
    res = preco/2
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

