resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número inteiro positivo: '))
    c = 1  # contador
    f = 1  # iniciando o fatorial
    while c <= n:
        f = f * c
        c = c + 1
    print(f)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('Fim do programa!')


# n = int(input('Digite um número inteiro: '))
# while n >= 0:
#     fatorial = 1
#     while n > 1:
#         fatorial = fatorial * n
#         n = n - 1
#     print(fatorial)
#     n = int(input('Digite um número inteiro: '))
