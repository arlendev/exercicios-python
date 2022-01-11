soma = 0
cont = 0
for nr in range(1, 501, 2):
   if nr % 3 == 0:
      soma += nr
      cont += 1
print('A soma de todos os {} valores solicitados é {}' .format(cont, soma))
print('FIM')