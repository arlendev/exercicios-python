from random import randint
from time import sleep
n = int(input('Pense em um número de 0 a 5: '))  # jogador tenta adivinhar
sorteio = randint(0, 5)  # faz o computador randomizar um número
print('PROCESSANDO ...')
sleep(2)
if n == sorteio:
   print('ACERTOU')
else: 
   print('ERROU')
print('O número era {}' .format(sorteio))
print('*FIM*')
