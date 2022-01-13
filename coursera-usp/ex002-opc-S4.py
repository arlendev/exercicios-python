# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

n = input('Digite um número inteiro:')

tamanho = len(n)
verifica = False
i = 0

while i < tamanho - 1:
    if n[i] == n[i + 1]:
        verifica = True
    i = i + 1
    
if verifica:
    print("sim")
else:
    print("não")
