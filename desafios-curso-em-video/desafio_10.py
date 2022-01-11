real = float(input('Informe quantos reais você tem na carteira: R$'))
dolar = real / 3.27
print('Com os seus R${:.2f} você pode comprar US${:.2f}' .format(real, dolar))