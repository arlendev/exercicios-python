from time import sleep

# from math import factorial
# nr = int(input('Digite um número para calcular o seu fatorial: '))
# fat = factorial(nr)
# print('Calculando ...')
# sleep(1)
# print('O fatorial de {} é: {}' .format(nr, fat))

nr = int(input('Digite um número para calcular o seu fatorial: '))
c = nr
f = 1
print('Calculando...')
sleep(1)
print('Fatorial de {}! = ' .format(nr), end='')
while c > 0:
   print('{}' .format(c), end=' ')
   print(' x ' if c> 1 else ' = ', end=' ')
   f *= c
   c-= 1
print('{}' .format(f))
