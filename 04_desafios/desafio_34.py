salario = float(input('Informe o seu salário: R$ '))
if salario > 1250:
   print('O seu salário de R$ {:.2f} com o aumento de 10% é R$ {:.2f}' .format(salario, salario * 1.10))
else:
   print('O seu salário de R$ {:.2f} com o aumento de 15% é R$ {:.2f}' .format(salario, salario * 1.15))
