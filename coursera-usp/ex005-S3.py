#verificando ordenação
num = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))
num2 = int(input('Digite mais um número: '))
if num < num1 < num2:
    print('crescente')
else:
    print('não está em ordem crescente')
