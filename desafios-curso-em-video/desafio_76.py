lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor',
            4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
   if pos % 2 == 0:
      print(f'{lista[pos]:.<30}', end='')
   else:
      print(f'R${lista[pos]:>7.2f}')
print('-' * 40)

#solução de um colega
# lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor',
#             4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
# titulo = 'LISTAGEM DE PREÇOS' #add um titulo para formatar
# print('-'*40)
# print('{:^40}'.format(titulo))
# print('-'*40)
# for cont in range(0, len(lista), 2): #para toda a tupla pulando de 2 em 2, imprimir um valor ao lado do seu sucessor
#     print('{:.<30}R$ {:>7.2f}'.format(lista[cont], lista[cont+1]))
# print('_'*40)