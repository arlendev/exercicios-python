somaidade = 0
médiaidade = 0
maioridadehomem = maisvelho = ''
totmulher20 = 0
for pessoa in range(1, 5):
   print('----- {}ª PESSOA -----' .format(pessoa))
   nome = str(input('Nome: ')).strip()
   idade = int(input('Idade: '))
   sexo = str(input('Sexo [M/F]: ')).strip()
   somaidade += idade
   if pessoa == 1 and sexo in 'Mm':
      maioridadehomem = idade
      nomemaisvelho = nome
   if sexo in 'Mm' and idade > maioridadehomem:
      maioridadehomem = idade
      nomemaisvelho = nome
   if sexo in 'Ff' and idade < 20:
      totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos' .format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.' .format(maioridadehomem, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(totmulher20))
