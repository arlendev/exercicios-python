#Distância entre dois pontos

from math import sqrt
x1 = int(input('Insira o ponto x1: '))
x2 = int(input('Insira o ponto x2: '))
y1 = int(input('Insira o ponto y1: '))
y2 = int(input('Insira o ponto y2: '))

dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(dist)
if dist >= 10:
    print('longe')
else:
    print('perto')
