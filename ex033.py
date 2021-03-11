n1 = int(input('Digite um ano para ver se ele é bissexto ou não: '))
b = int(n1%4)
c = int(n1%400)
d = int(n1%100)
if b > 0:
    print('O ano de {} é bissexto!'.format(n1))
elif c > 0:
    print('O ano de {} é bissexto!'.format(n1))
elif d > 0:
    print('O ano de {} é bissexto!'.format(n1))
else:
    print('O ano de {} não é bissexto!'.format(n1))
