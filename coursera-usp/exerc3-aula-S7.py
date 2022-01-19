def éPrimo(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x / 2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

n = int(input('Digite um número inteiro (999 para parar): '))

while n > 0:
    if n == 999:
        break
    if éPrimo(n):
        print(n, 'é primo!')
    else:
        print(n, 'não é primo :-(')
    n = int(input('Digite um número inteiro (999 para parar): '))

print('Fim do programa!')