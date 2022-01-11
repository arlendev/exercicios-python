preco = float(input('Informe o preço do produto: R$ '))
desc = float(preco * 0.95)
print('O preço deste produto que custava R${:.2f}, na promoção com 5% de desconto é R${:.2f}' .format(preco, desc))
