from ex108_modulo import moeda

valor = float(input('Informe um valor: R$'))

print(f'Aumento de 10%: {moeda.aumentar(valor, 10)}')
print(f'Rezudino 15%: {moeda.diminuir(valor, 15)}')
print(f'O dobro de {moeda.moeda(valor, "$")} é: {moeda.dobro(valor)}')
print(f'A metade de {moeda.moeda(valor)} é: {moeda.metade(valor)}')