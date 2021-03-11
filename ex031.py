n1 = (int(input('Escolha um número para ver se é par ou ímpar: ')))
r = int(n1%2)
if r > 0:
    print('O resto da divisão de {} é {} que é impar.'.format(n1, r))
else:
        print('O resto da divisão de {} é {} que é par'.format(n1, r))
