cont = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
   nr = int(input('Digite um número de 0 a 20: '))
   if 0 <= nr <= 20:
      break
   print('Tete novamente. ', end='')
print(f'Você digitou o número {cont[nr]}.')

# solução de um colega
# num = int(input('Digite um valor entre 0 e 20: '))
# if num > 20 or num < 0:
#     print('Valor não aceito. Tente novamente.')
#     num = int(input('Digite um valor entre 0 e 20: '))
# extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
# print(f'Você digitou o número {extenso[num]}')

# outras solução de colega
# numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# while True:
#     n = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= n <= 20:
#         print(f'O número escolhido foi {numeros[n]}')
#         break
#     else:
#         print(f'{n} não está entre 0 e 20.')

# solução 3
# extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
#            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
#            'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
#            'Quinze', 'Dizesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
# r = 'S'
# while True:
#     while True:
#         n = int(input('Digite um número de 0 a 20: '))
#         if 0 <= n <= 20:
#             print(f'O número \033[32m{n}\033[m em extenso é: \033[32m{extenso[n]}\033[m')
#             break
#         else:
#             print('Digite o número novamente!')

#     r = str(input('Deseja continuar, "S" para sim e "N" para não: ')).strip().upper()
#     if r == 'N':
#         break
# print('-=- Programa encerrado -=-')
