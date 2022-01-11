from random import randint
print('Sou o seu computador ...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
computador = randint(0, 10)  # faz o computador randomizar um número
acertou = False
palpites = 0
while not acertou:
   jogador = int(input('Qual é o seu palpite? '))
   palpites += 1
   if jogador == computador:
      acertou = True
   else:
      if jogador < computador:
         print('Mais... Tente mais uma vez.')
      elif jogador > computador:
         print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!' .format(palpites))
