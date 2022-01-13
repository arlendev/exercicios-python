# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

n = int(input('Digite um número inteiro: '))
cont = 2
primo = True

while (cont < n and primo):
    primo = not ((n % cont) == 0)
    cont = cont + 1
if (primo):
    print('primo')
else:
    print('não primo')
