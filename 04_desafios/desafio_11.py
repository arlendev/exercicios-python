larg = float(input('Informa a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
area = larg * alt
print('A sua parede tem a dimensão de {:.2f}m x {:.2f}m e a sua área é de {:.2f}m2' .format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede de {:.2f}m2 você vai precisar de {:.2f}l de tinta' .format(area, tinta))
