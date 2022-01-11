distancia = float(input('Informe a distância a ser percorrida na viagem: '))
if distancia <= 200:
   preço = distancia * 0.50
else:
   preço = distancia * 0.45
print('A sua viagem tem {} km e o seu preço é de R$ {}' .format(distancia, preço))
print('Boa viagem!')

''' segunda forma de escrever este programa
distancia = float(input('Informe a distância a ser percorrida na viagem: '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('A sua viagem tem {} km e o seu preço é de R$ {}' .format(distancia, preço))
print('Boa viagem!')