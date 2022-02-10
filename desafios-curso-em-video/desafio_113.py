def resumo(preco=0, aum=0, red=0):
    print('--' * 15)
    print(f'{"RESUMO DO VALOR":^30}')
    print('--' * 15)
    res = preco
    aumento = aum
    reducao = red

    print(f'{"Preço Analisado:":<20} {moeda(res)}')
    print(f'{"Dobro do Preço:":<20} {moeda(dobro(res))}')
    print(f'{"Metade do Preço:":<20} {moeda(metade(res))}')
    print(f'{aum}{"% de aumento:":<18} {moeda(aumentar(res, aumento))}')
    print(f'{reducao}{"% de redução:":<18} {moeda(diminuir(res, reducao))}')
    print('--' * 15)
