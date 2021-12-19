peso = float(input('Informe o seu peso: (kg) '))
altura = float((input('Informe a sua altura: (m) ')))
imc = peso / (altura * altura)   # ou (altura ** 2)
print('O seu peso é {} kg e a sua altura é {} m.' .format(peso, altura))
print('Seu IMC é de {:.2f}' .format(imc))
if imc < 18.5:
   print('Você está abaixo do peso.')
elif imc < 25:   # ou 18.5 <= imc < 25
   print('Seu peso é ideal.')
elif imc < 30:
   print('Você está com sobrepeso.')
elif imc < 40:
   print('VocÊ está com obesidade.')
else:
   print('Você está com obesidade mórbida.')
