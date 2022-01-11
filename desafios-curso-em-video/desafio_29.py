vel = float(input('A velocidade do carro é: '))
print('A sua velocidade é de {} km/h' .format(vel))
multa = (vel - 80) * 7
if vel > 80:
   print('Você excedeu o limite de velocidade, a sua multa é de R$ {:.2f}' .format(multa))
else:
   print('Você está detro do limite de velocidade de 80 km/h, tenha um bom dia!')
print('Dirija sempre com segurança!')
