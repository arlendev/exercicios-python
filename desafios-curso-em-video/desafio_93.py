# jogador = {}
# partidas = []
# jogador['nome'] = str(input('Nome do Jogador: '))
# tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# for c in range(0, tot):
#    partidas.append(int(input(f'  Quantos gols na partida {c+1} ? ' )))
# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)
# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
# for k, v in jogador.items():
#    print(f'O campo {k} tem o valor {v}')
# print('-=' * 30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador['gols']):
#    print(f'   => Na partida {i}, fez {v} gols.')
# print(f'Foi um total de {jogador["total"]} gols.')


print('-'*12, end = '')
print('JOGADORES DE FUT', end = '')
print('-'*12)

jogador = dict()

jogador['nome' ] = input('Nome do jogador: ')
jogador['partidas'] = int(input('Partidas jogadas: '))
jogador['gols'] = []
#DEFININDO OS GOLS
for c in range(0, jogador['partidas']):
    jogador['gols'].append(int(input(f' Gols na {c+1}ª partida: ')))
jogador['total'] = sum(jogador['gols'])

print(f'O jogador {jogador["nome"]} fez um total de {jogador["total"]} gols nas suas {jogador["partidas"]} partidas.')
for k, s in enumerate(jogador['gols']):
    print(f'Partida {k+1}: {s} gols;')