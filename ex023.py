from math import cos, sin, tan, radians
an = int(input('Digite um ângulo: '))
s = sin(radians(an))
c = cos(radians(an))
t = tan(radians(an))
print('o valor do seno é:{:.2f} \n o valor do cosseno é: {:.2f} \n o valor da tangente é: {:.2f} '.format(s, c, t))
