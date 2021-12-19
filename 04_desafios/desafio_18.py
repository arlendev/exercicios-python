import math
ang = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(ang))  # coverter o ângulo para radianos
print('O ângulo de {}º tem o SENO de {:.2f}' .format(ang, seno))
coss = math.cos(math.radians(ang))  # coverter o ângulo para radianos
print('O ângulo de {}º tem o COSSENO de {:.2f}' .format(ang, coss))
tang = math.tan(math.radians(ang))  # coverter o ângulo para radianos
print('O ângulo de {}º tem a TANGENTE de {:.2f}' .format(ang, tang))