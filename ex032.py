print('----------Agência de viagens Will----------')
n1 = int(input('Qual a distância da viagem em km que você quer percorrer?'))
if n1<= 200:
    d1 = float(n1 * 0.50)
    print('O preço de sua viagem irá sair por: {}'.format(d1))
else:
    d2 = float(n1 * 0.45)
    print('O preço da sua viagem irá sair por: {}'.format(d2))
    