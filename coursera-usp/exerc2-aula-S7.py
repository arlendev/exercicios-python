c = f = 1
while True:
    n = int(input('Digite um número inteiro positivo (999 para parar): '))
    if n == 999:
        break
    while c <= n:
        f = f * c
        c = c + 1
    print(f)
print('Fim do programa!')
