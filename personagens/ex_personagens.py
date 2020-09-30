## 1 - Exibindo dados

import csv

ps = open('personagens.csv', 'r')

ler = csv.reader(ps)

for row in ler:
    print(row)
    
ps.close()
    
## 2 - Recriando dados

novo_ps = open('personagens_novo.csv', 'w')

titulos = ['Nome', 'Parece humano', 'É intrinsecamente mau', 'É capitalista']

escrever = csv.DictWriter(novo_ps, fieldnames = titulos)
escrever.writeheader()
escrever.writerow({'Nome': 'Mônica', 'Parece humano': 'Sim', 'É intrinsecamente mau': 'Não', 'É capitalista': 'Não'})
escrever.writerow({'Nome': 'Italo', 'Parece humano': 'Sim', 'É intrinsecamente mau': 'Não', 'É capitalista': 'Sim'})

novo_ps.close()