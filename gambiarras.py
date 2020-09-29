############################################################################

errado = open('errado.csv')
errado = ''.join([i for i in errado]).replace('Qualquer federal', 'UFSCar')
errado = ''.join([i for i in errado]).replace('na cozinha', 'onde ela quiser')

certo = open('certo.csv', 'w')

certo.writelines(errado)

