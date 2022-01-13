#Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

c = 0 #contador
n = int(input('Digite o valor de n: '))
while c < n: 
    print(2*c + 1)
    c = c + 1