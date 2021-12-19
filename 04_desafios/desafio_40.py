nota1 = float(input('Digite a sua prmeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
média = (nota1 + nota2) / 2
if média >= 7:
    print('Tirando {} e {}, a média do aluno é \033[0;32m{}\033[m.' .format(nota1, nota2, média))
    print('O aluno está \033[0;32mAPROVADO!\033[m')
elif 7 > média >= 5:
    print('Tirando {} e {}, a média do aluno é \033[0;33m{}\033[m.' .format(nota1, nota2, média))
    print('O aluno está em \033[0;33mRECUPERAÇÃO!\033[m')
elif média <= 5:
    print('Tirando {} e {}, a média do aluno é \033[0;31m{}\033[m.' .format(nota1, nota2, média))
    print('O aluno está \033[0;31mREPROVADO!\033[m')
