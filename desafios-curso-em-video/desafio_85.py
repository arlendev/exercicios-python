nrs = [[], []]
valor = 0
for c in range(1, 8):   # c = contador
   valor = int(input(f'Digite o {c}º valor: '))
   if valor % 2 == 0:
      nrs[0].append(valor)
   else:
      nrs[1].append(valor)
print('-=' * 30)
nrs[0].sort()
nrs[1].sort()
print(f'Todos os valores: {nrs}')
print(f'Os números pares são {nrs[0]}')
print(f'Os números ímpares são {nrs[1]}')
