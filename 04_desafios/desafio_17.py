'''
catOpo = float(input('Insira o cateto oposto: '))
catAdj = float(input('Insira o cateto adjacente: '))
hip = (catOpo ** 2 + catAdj ** 2) ** (1/2)

print('O valor da hipotenusa entre {:.2f} e {:.2f} é: {:.2f}' .format(catOpo, catAdj, hip))
'''

from math import hypot
import math
catOpo = float(input('Insira o cateto oposto: '))
catAdj = float(input('Insira o cateto adjacente: '))
hip = math.hypot(catOpo, catAdj)

print('O valor da hipotenusa entre {:.2f} e {:.2f} é: {:.2f}' .format(catOpo, catAdj, hip))