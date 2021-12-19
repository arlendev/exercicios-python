print('{:=^40}' .format(' LOJAS GUANABARA '))
preço = float(input('Insira o preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque')
[ 2 ] ã vista cartão')
[ 3 ] 2x no cartão')
[ 4 ] 3x ou m ais no cartão''')
cond = int(input('Insira a condição desejada: '))
if cond == 1:
   print('Para as suas compras de R$ {:.2f}, o pagamento à vista (dinheiro / cheque) é de R$ {:.2f}' .format(preço, preço * 0.9))
elif cond == 2:
   print('Para as suas compras de R$ {:.2f}, o pagamento à vista (cartão) é de R$ {:.2f}' .format(preço, preço * 0.95))
elif cond == 3:
   parcela = preço / 2
   print('Para as suas compras de R$ {:.2f}, o pagamento no cartão é de 2x R$ {:.2f}' .format(preço, parcela))
elif cond == 4:
   totparc = int(input('Insira o número de parcelas desejadas: '))
   parcela = (preço * 1.2) / totparc
   print('Para as suas compras de R$ {:.2f}, o pagamento no cartão é de {}x R$ {:.2f}' .format(preço, totparc, parcela))
else:
   print('Opção inválida de pagamento, tente novamente.')
