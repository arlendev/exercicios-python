# estrutura de entrada de dados
time = []
jogador = {}
partidas = []

while True:
   jogador.clear()
   jogador['nome'] = str(input('Nome do Jogador: '))
   tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
   partidas.clear()
   for c in range(0, tot):
      partidas.append(int(input(f'  Quantos gols na partida {c+1} ? ' )))
   jogador['gols'] = partidas[:]
   jogador['total'] = sum(partidas)
   time.append(jogador.copy())
   while True:
      resp = str(input('Quer continuar? [S/N] ')).upper()[0]
      if resp in 'SN':
         break
      print('ERRO! Responda apenas S ou N.')
   if resp == 'N':
      break

# estrutura de saída de dados (análise e resultado)
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
   print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
   print(f'{k:>3} ', end='')
   for d in v.values():
      print(f'{str(d):<15}', end='')
   print()
print('-' * 40)
while True:
   busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
   if busca == 999:
      break
   if busca >= len(time):
      print(f'ERRO! Não existe jogador com código {busca}!')
   else:
      print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
      for i, g in enumerate(time[busca]['gols']):
         print(f'   No jogo {i+1} fez {g} gols.')
   print('-' * 40)
print('<< VOLTE SEMPRE >>')

'''
individual = dict()
jogadores = list()
temp = list()
jogos = list()
gols = list()
print('-=' * 26 + '-')
while True:
    individual.clear()
    individual['Jogador'] = str(input('Nome: ')).strip().capitalize()
    individual['Jogos'] = int(input(f'Quantos jogos {individual["Jogador"]} jogou? '))
    for c in range(individual['Jogos']):
        gol = (int(input(f'Digite quantos gols ele fez na {c+1}ª partida: ')))
        temp.append(gol)
    print('-=' * 26 + '-')
    jogos.append(individual['Jogos'])
    gols.append(temp[:])
    individual['Gols'] = temp.copy()
    individual['Total'] = sum(temp)
    temp.clear()
    jogadores.append(individual.copy())
    while True:
        o = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if o in 'SN':
            break
        print('ERRO! Digite apenas S ou N!')
    if o == 'N':
        break
print('-=' * 26 + '-')
print(f'{"Cód"} {"Nome":<15} {"Gols":<25} {"Total":<25}')
print('-=' * 26 + '-')
for k, v in enumerate(jogadores):
    print(f'({str(k)}) {str(v["Jogador"]):<15} {str(v["Gols"]):<25} {str(v["Total"]):<25}')
print('-=' * 26 + '-')

while True:
    e = int(input('Digite o código do jogador a ser analisado (999 finaliza): '))
    if e in range(len(jogadores)) and e != 999:
        print(f'O jogador: {jogadores[e]["Jogador"]} marcou:')
        for c in range(jogos[e]):
            print(f' -> Na {c+1}ª partida, marcou: {gols[e][c]} gols')
        print('-=' * 26 + '-')
    elif e == 999:
        print('-=' * 26 + '-')
        break
    else:
        print('Código ERRADO! Digite novalmente!')
print(f'{"<< FINALIZADO >>":^33}')
'''