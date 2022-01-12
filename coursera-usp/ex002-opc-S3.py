#escreva um programa que calcula as raízes de uma equação do segundo grau
from math import sqrt

a = float(input('Digite um valor para a: '))
b = float(input('Digite um valor para b: '))
c = float(input('Digite um valor para c: '))

d = (b*b)-(4*a*c)

if d < 0:
 print('esta equação não possui raízes reais.')
elif d == 0:
 raiz1 = ((-1*b) + sqrt(d))/(2*a)
 print(f'a raiz desta equação é {raiz1}')
else:
 raiz1 = ((-1*b)+sqrt(d))/(2*a)
 raiz2 = ((-1*b)-sqrt(d))/(2*a)
 if raiz1<raiz2:
  print(f'as raízes da equação são {raiz1} e {raiz2}')
 else:
  print(f'as raízes da equação são {raiz2} e {raiz1}')
