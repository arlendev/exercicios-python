# def leiaInt(msg):
#    ok = False
#    valor = 0
#    while True:
#       n = str(input(msg))
#       if n.isnumeric():
#          valor = int(n)
#          ok = True
#       else:
#          print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
#       if ok:
#          break
#    return valor


# #Programa principal
# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')
# print('FIM')

def LeiaInt(pergunta):
    while True:
        number = str(input('Digite um número: '))
        if number.isnumeric():
            return number
        else:
            print('\033[;31mERRO! Digite um número inteiro válido.\033[m')


n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')