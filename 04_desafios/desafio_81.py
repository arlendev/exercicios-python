lista = []
while True:
   n = int(input('Digite um valor: '))
   if n not in lista:
      lista.append(n)
      print('\33[0;32mValor adicionado com suesso!\33[m')
   else:
      print('\33[0;31mValor duplicado! Não vou adicionar na lista!\033[m')
   resp = str(input('Quer continuar? [S/N] '))
   if resp in 'Nn':
      break
print('-=' * 30)
print(f'Você digtou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'\33[0;33mOs valores em ordem decrescente são {lista}\033[m')
if 5 in lista:
   print('\33[0;32mO valor 5 faz parte da lista!\033[m')
else:
   print('\33[0;31mO valor 5 não foi encontrado na lista!\033[m')