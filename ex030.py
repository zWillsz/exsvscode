import random
print('----------Jogo da Advinhação v1.0----------')
n1 = int(input('Escreva um número de 0 a 5: '))
num1 = int(0)
num2 = int(1)
num3 = int(2)
num4 = int(3)
num5 = int(4)
num6 = int(5)
lista = (num1, num2, num3, num4, num5, num6)
resultado = random.choice(lista)
if n1 == resultado:
 print('O número sorteado foi: {}\n E o número escolhido foi: {}\n Parabéns você acertou!'.format(resultado, n1))
else:
    print('O número sorteado foi: {}\n E o número escolhido foi:{}\n Infelizmente você não acertou, tente novamente!'.format(resultado, n1))
