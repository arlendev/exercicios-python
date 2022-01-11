print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Insira o comprimento da primeira reta: '))
r2 = float(input('Insira o comprimento da segunda reta: '))
r3 = float(input('Insira o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
   if r1 == r2 == r3:
      print('EQUILÁTERO (todos os lados iguais).')
   elif r1 != r2 != r3 != r1:
      print('ESCALENO (todos os lados diferentes).')
   else:
      print('ISÓSCELES (dois lados iguais).')
else:
    print('Os segmentos informados NÃO PODEM FORMAR triângulo!')
