emprestimo = float(input('Informe qual o valor do empréstimo desejado: '))
salario = float(input('Informe qual é o seu salário: R$ '))
periodo = int(input('Informe em quantos anos você deseja pagar: '))
parcela = emprestimo / (periodo * 12)
print('Para pegar um empréstimo de R$ \033[1;31m{:.2f}\033[m em \033[1;31m{}\033[m anos, a prestação será de R$ \033[1;31m{:.2f}\033[m' .format(emprestimo, periodo, parcela))
if parcela <= salario *0.3: 
   print('O seu salário R$ \033[1;31m{:.2f}\033[m não é suficiente, o empréstimo \033[1;31mFOI NEGADO!\033[m' .format(salario))
else:
   print('O seu salário R$ \033[1;32m{:.2f}\033[m está de acordo, o empréstimo \033[1;32mFOI APROVADO!\033[m' .format(salario))   