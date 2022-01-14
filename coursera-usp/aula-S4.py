# i = 0
# while i <= 20:
#     print(2 ** i)
#     i = i + 1
#===================================================================================
# print('Digite uma sequência de valores terminada por zero.')
# soma = 0
# valor = 1
# while valor != 0:
#     valor = int(input('Digite um valor a ser somado: '))
#     soma = soma + valor
# print(f'A soma dos valores digitados é {soma}')
#===================================================================================
# print('Digite uma sequência de valores terminada por zero.')
# produto = 1
# valor = 1
# while valor != 0:
#     valor = int(input('Digite um valor a ser multiplicado: '))
#     produto = produto * valor
# print(f'A multiplicação dos valores digitados é {produto}')
#===================================================================================
tamanho = int(input('Digite quantos números você quer multiplicar: '))
produto = 1
i = 0
while i < tamanho:
    valor = int(input('Digite o valor a ser multiplicado: '))
    produto = produto * valor
    i = i + 1
print(f'O produto dos valores digitados é: {produto}')
#===================================================================================
