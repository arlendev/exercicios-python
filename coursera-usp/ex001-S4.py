# Escreva um programa que receba um número natural  n na entrada e imprima  n!(fatorial) na saída.

c = 1  #contador
fat = 1  
n = int(input('Digite o valor de n: '))

while c <= n:
    fat = fat * c
    c = c + 1

print(fat)
