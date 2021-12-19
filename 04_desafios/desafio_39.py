from datetime import date
atual = date.today().year
nasc = int((input('Insira o ano do seu nascimento: ')))
idade = atual - nasc
sexo = str(input('Qual o seu sexo (M ou F)? '))
if sexo == 'f':
    print('Você não precisa se alistar, o alistamento obrigatório é somente para os homens.')
else:
    print('Quem nasceu em {} tem {} anos em {}.' .format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o seu alistamento.' .format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.' .format(ano))
    elif idade > 18: # poderia usar else aqui
        saldo = idade - 18
        print('Você já deveria tem se alistado há {} anos.' .format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.' .format(ano))
    