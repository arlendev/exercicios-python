dias = float(input('Informa o número de dias que foi alugado o carro: '))
km = float(input('Informa a kilometragem percorrida com o carro: '))
pago = (dias * 60) + (km * 0.15)
print('Você alugou o carro por {:.0f} dias e percorreu {:.2f} km. O valor total a ser pago pela locação é de R${:.2f}.' .format(dias, km, pago))