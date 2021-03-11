n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite outro valor: '))
# Vendo quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
    print('O maior é: {}'.format(n2))
elif n3 > n1 and n3 > n2:
    maior = n3
    print('O maior é: {}'.format(n3))
# Vendo quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    print('O menor é: {}'.format(n2))
elif n3 < n1 and n3 < n2:
    print('O menor é: {}'.format(n3))
