# num = int(input('Insira um número: '))
# print(num *2)
# print(num *3)
# print((num)**0.5) / num

n = int(input('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)  # ou pow(n, (1/2))
print('O dobro de {} vale {}, o seu triplo é {} e a raiz quadrada é {:.2f}.' .format(n, d, t, r))