frase = str(input('Digite uma frase: ')).strip().upper()  # strip remove espaços antes e depois e upper para tuto em maiúsculo
palavras = frase.split()
junto = '' .join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
   inverso += junto[letra]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
   print('Temos um palíndromo !')
else:
   print('A frase digitada não é um palíndromo !')

# somente no python dá para fazer este exercício de outra forma

frase = str(input('Digite uma frase: ')).strip().upper()  # strip remove espaços antes e depois e upper para tuto em maiúsculo
palavras = frase.split()
junto = '' .join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
   print('Temos um palíndromo !')
else:
   print('A frase digitada não é um palíndromo !')