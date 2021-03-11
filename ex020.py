import random
or1 = input('Primeira Ordem: ')
or2 = input('Segunda Ordem: ')
or3 = input('Terceira Ordem: ')
or4 = input('Quarta Ordem: ')
lista = (or1, or2, or3, or4)
resultado = random.choice(lista)
print('A ordem de apresentacão será: {}'.format(resultado))
