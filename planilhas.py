## DOCUMENTÃO DE PLANILHAS

import csv

# Escrevendo com csv.writer

# Abrindo a planilha - Se ela existir, abre em modo de escrita. Se não existir, cria-se uma planilha com esse nome
planilha = open('teste.csv', 'w')

#Criando o objeto de escrita
escrever = csv.writer(planilha)

#Utilizando o obj de escrita para escrever na planilha    
escrever.writerow(['Nome', 'PyLadies'])
escrever.writerow(['Alexandra', 'PyLadies São Carlos'])
escrever.writerow(['Marcella', 'PyLadies Paraíba'])

# Fechando a planilha
planilha.close()

#Escrevendo com dicionários

planilha = open('dicionarios.csv', 'w')

titulos = ['Nome', 'Capítulo', 'Banda favorita']

#Parâmetros obrigatorios: nome da planilha e chaves do dicionário
escrever = csv.DictWriter(planilha, fieldnames=titulos)

#Escrevendo as chaves como cabeçalho - opcional
escrever.writeheader()

escrever.writerow({'Nome': 'Amanda', 'Capítulo': 'PyLadies São Carlos', 'Banda favorita': 'Os Barões da Pisadinha'})
escrever.writerow({'Nome': 'Marcella', 'Capítulo': 'PyLadies Paraíba', 'Banda favorita': 'Maroon 5'})

planilha.close()

#Lendo e exibindo
planilha_2 = open('teste.csv')

ler = csv.reader(planilha_2)

for row in ler:
    print(row[0], ' - ', row[1]) # Aqui exibimos o elemento da coluna 0 - elemento da coluna 1

planilha_2.close()

#Exemplo cabeçalho
planilha = open('teste.csv')

# Abrindo listas vazias, onde ficarão as linhas da planilha
cabecalho = []
proxs = []

# Lemos a primeira linha, salvamos em 'cabecalho' e avançamos uma linha
cabecalho = next(ler)
# Lemos a proxima linha, salvamos em 'proxs' e avançamos mais uma linha
proxs = next(ler)

print("O cabeçalho é:", cabecalho)
print("Proximos: ", proxs)
  
planilha.close()

# Lendo com dicionários
planilha = open('dicionarios.csv')

ler = csv.DictReader(planilha)
for row in ler:
    # Podemos usar as chaves do dicionário para exibir os valores
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
print("Nº de linhas lidas: ", leitura.line_num) # Como acabamos de abrir o arquivo, a linha atual é 0

total = 0
leitura.__next__()

for row in leitura:
    total += float(row[0])
    total += float(row[1])
    total += float(row[2])
print(total)

print("Nº de linhas lidas: ", leitura.line_num) #Agora, depois de ler todas as linhas de contas.csv, a linha atual é 3 (depois de todos os valores)