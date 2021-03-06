n1 = int(input('nota 1 bimestre: '))
n2 = int(input('nota 2 bimestre: '))
n3 = int(input('nota 3 bimestre: '))
n4 = int(input('nota 4 bimestre: '))
m = int((n1 + n2 + n3 +n4) / 4)
print('a média do aluno é {}'.format(m))
if m > 6:
 print('APROVADO!')
else:
 print('REPROVADO!')
