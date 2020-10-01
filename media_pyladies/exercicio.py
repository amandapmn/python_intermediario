import csv

planilha = open('pyladies.csv', 'w')

titulo = ['Nome', 'Capítulo', 'Idade']

escrever = csv.writer(planilha)
escrever.writerow(titulo)
escrever.writerow(['Amanda', 'São Carlos', '20'])
escrever.writerow(['Cissa', 'São Carlos', '40'])
escrever.writerow(['Mariana', 'Recife', '32'])

planilha.close()

planilha = open('pyladies.csv')
total = 0
#lidos = 0

ler = csv.reader(planilha)
ler.__next__()
for row in ler:
    print(row[0], '-', row[1], '-', row[2])
    total += int(row[2])
    #lidos += 1

lidos = (ler.line_num) - 1

media = total/lidos

print(media)

