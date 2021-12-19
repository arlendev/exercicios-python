from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opção = 0
while opção != 5:
   print('''   [ 1 ] somar
   [ 2 ] multiplicar
   [ 3 ] maior
   [ 4 ] novos números
   [ 5 ] sair do programa''')
   opção = int(input('>>>>> Insira qual a sua opção: '))
   if opção == 1:
      somar = n1 + n2
      print('A soma entre {} + {} é {}' .format(n1, n2, somar))
   elif opção == 2:
      multiplicar = n1 * n2
      print('A multiplicação entre {} * {} é {}' .format(n1, n2, multiplicar))
   elif opção == 3:
      if n1 > n2:
         maior = n1
      else:
         maior = n2
      print('Entre {} e {} o maior valor é {}' .format(n1, n2, maior))
   elif opção == 4:
      print('Informe os números novamente: ')
      n1 = int(input('Digite um número: '))
      n2 = int(input('Digite outro número: '))
   elif opção == 5:
      print('Finalizando ...')
   else:
      print('Opção inválida. Tente novamente.')
   print('=-=' * 10)
   sleep(2)
print('FIM DO PROGRAMA!')
