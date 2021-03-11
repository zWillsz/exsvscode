from math import hypot
cop = int(input('Comprimento de um número inteiro do cateto oposto: '))
caj = int(input('Comprimento de um número inteiro do cateto adjascente: '))
h = hypot(cop, caj)
print('O comprimento da hipotenusa de números inteiros é : {:.2f}'.format(h))
cop2 = float(input('Comprimento de um número decimal do cateto oposto: '))
caj2 = float(input('Comprimento de um número decimal do cateto adjascente: '))
h2 = hypot(cop2, caj2)
print('O comprimento da hipotenusa de números decimais é: {:.2f}'.format(h2))
