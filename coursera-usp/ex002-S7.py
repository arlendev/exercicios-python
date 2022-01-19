'''
Exercício 2
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
'''

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
linha = 0
while linha < altura:
    coluna = 0
    while coluna < largura:
        if linha == 0 or linha == altura-1 or coluna == 0 or coluna == largura-1:
            print("#"  ,end = "")
        else:
            print(" ",end = "")
        coluna = coluna + 1
    print()
    linha = linha + 1