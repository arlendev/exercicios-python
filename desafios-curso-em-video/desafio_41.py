from datetime import date
atual = date.today().year
nasc = int(input('Informe o seu ano de nascimento: '))
idade = atual - nasc
print('Ano de nascimento: {}' .format(nasc))
print('O atleta tem {} anos.' .format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:   # ou else:
    print('Classificação: MASTER')
