segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = segundos // 86400
segundos_resto = segundos % 86400
horas = segundos_resto // 3600
segundos_resto = segundos_resto % 3600
minutos = segundos_resto // 60
segundos_resto = segundos_resto % 60

print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos_resto} segundos.')