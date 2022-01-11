boletim = [[], [], [], []]
print('-=' * 35 + '-')
while True:
    o = ' '
    nome = str(input('Insira o nome do aluno: ')).capitalize()
    n1 = float(input(f'Insira a 1ª nota de {nome}: '))
    n2 = float(input(f'Insira a 2ª nota de {nome}: '))

    boletim[0].append(nome)
    boletim[1].append(n1)
    boletim[2].append(n2)
    boletim[3].append((n1 + n2)/2)

    while o not in 'SN':
        o = str(input('Deseja continuar? [S/N]: ')).upper()
    if o == 'N':
        break
    print('-=' * 35 + '-')
print('-=' * 35 + '-')
print(f'{"N°":<4}  {"Aluno":<8}   {"Média":>8}')
for i, c in enumerate(boletim[0]):
    print(f'{i:<4} {boletim[0][i]:<10} {boletim[3][i]:>8.2f}')
print('-=' * 35 + '-')
while True:
    m = int(input('Insira o número do aluno que se deseja conferir às notas(999 saí): '))
    if m in range(len(boletim[1])):
        print(f'O aluno: \033[32m{boletim[0][m]}\033[m '
f'teve às seguintes notas: \033[32m{boletim[1][m]}\033[m e \033[32m{boletim[2][m]}\033[m')
        print('-=' * 35 + '-')
    if m == 999:
        print('-=' * 35 + '-')
        break