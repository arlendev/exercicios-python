from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for nasc in range(1, 7):
   nasc = int(input('Insira a {}ª data de nascimento: ' .format(nasc)))
   idade = atual - nasc
   if idade < 18:
      totmenor += 1
   else:
      totmaior += 1
print('Ao todo tivemos {} pessoas menores de idade e {} pessoas maiores de idade.' .format(totmenor, totmaior))
