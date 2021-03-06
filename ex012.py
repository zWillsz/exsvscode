d = int(input('quantos reais voce tem na carteira?'))
Valor_em_dolares = 3.27
if d > Valor_em_dolares:
 print('Você pode comprar {:.2f}US$'.format(d / Valor_em_dolares))
else:
 print('Você não tem dinheiro o suficiente para comprar um dólar!')
