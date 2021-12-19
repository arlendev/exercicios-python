nome = str(input('Digite o seu nome completo: ')).strip()  
# explicitar que é uma str e o strip elimina todos os espaços antes e depois do str
print('Analisando o seu nome ...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))