salario = int(input('Qual o seu salário: R$ '))
if salario > 1250:
 c = int(salario * 1.10)
 print('O seu novo salário é: R${}'.format(c))
# Ajustando salários mais baixos
if salario <= 1250:
    c2 = int(salario * 1.15)
    print('O seu novo salário é: R${}'.format(c2))
