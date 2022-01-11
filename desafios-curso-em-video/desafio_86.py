matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# este bloco é para preencher a patriz
for l in range(0, 3):  # um for na linha
   for c in range(0, 3):  # um for na coluna, dentro da linha
      matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# este bloco é mostrar a matriz na tela
print('-=' * 30)
for l in range(0, 3):
   for c in range(0, 3):
      print(f'[{matriz[l][c]:^5}]', end='')  # :^5 centralizado com 5 caracteres
   print()
print('-=' * 30)