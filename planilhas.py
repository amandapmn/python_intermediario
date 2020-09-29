## DOCUMENTÃO DE PLANILHAS

import csv

# Escrevendo
planilha = open('teste.csv', 'w')
    
escrever = csv.writer(planilha)    
escrever.writerow(['Nome', 'PyLadies'])
escrever.writerow(['Alexandra', 'PyLadies São Carlos'])
escrever.writerow(['Marcella', 'PyLadies Paraíba'])

planilha.close()

#Escrevendo com dicionários

planilha = open('dicionarios.csv', 'w')

titulos = ['Nome', 'Capítulo', 'Banda favorita']

escrever = csv.DictWriter(planilha, fieldnames=titulos)
escrever.writeheader()
escrever.writerow({'Nome': 'Amanda', 'Capítulo': 'PyLadies São Carlos', 'Banda favorita': 'Os Barões da Pisadinha'})
escrever.writerow({'Nome': 'Marcella', 'Capítulo': 'PyLadies Paraíba', 'Banda favorita': 'Maroon 5'})

planilha.close()

#Lendo e exibindo
planilha = open('teste.csv')

ler = csv.reader(planilha)
for row in ler:
    print(row[0], ' - ', row[1])

pĺanilha.close()

#Exemplo cabeçalho
planilha = open('teste.csv')

cabecalho = []
proxs = []

cabecalho = next(ler)
proxs = next(ler)

print("O cabeçalho é:", cabecalho)
print("Proximos: ", proxs)
  
planilha.close()

# Lendo com dicionários
planilha = open('dicionarios.csv')

ler = csv.DictReader(planilha)
for row in ler:
    print(row['Nome'], '-', row['Capítulo'], '-', row['Banda favorita'])


#Fazendo contas - escrevendo valores

continhas = open('contas.csv', 'w')

escrever = csv.writer(continhas)
escrever.writerow(['Valores'])
escrever.writerow([2.0, 3.3, 7.2])
escrever.writerow([5.5, 1.1, 2.0])

continhas.close()

# Fazendo contas - lendo e somando valores

continhas = open('contas.csv')

leitura = csv.reader(continhas)
print("Nº de linhas lidas: ", leitura.line_num)

total = 0
leitura.__next__()

for row in leitura:
    total += float(row[0])
    total += float(row[1])
    total += float(row[2])
print(total)

print("Nº de linhas lidas: ", leitura.line_num)