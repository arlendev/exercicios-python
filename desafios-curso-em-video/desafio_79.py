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
lista.sort()
print(f'\33[0;33mVocê digitou os valores {lista}\033[m')
