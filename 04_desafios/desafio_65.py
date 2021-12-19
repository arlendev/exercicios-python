resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
   nr = int(input('Digite um número: '))
   soma += nr
   quant += 1
   if quant ==1:
      maior = menor = nr
   else:
      if nr > maior:
         maior = nr
      if nr < menor:
         menor = nr
   resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}.' .format(quant, média))
print('O maior valor digitado foi {} e o menor valor digitado foi {}.' .format(maior, menor))
