'''Exercício 2 - Máximo com 3 parâmetros
Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.
'''


def maximo(nr1, nr2, nr3):
    if nr1 > nr2 and nr1 > nr3:
        return nr1
    elif nr2 > nr1 and nr2 > nr3:
        return nr2
    else:
        return nr3

print(maximo(4, 2, 6))
