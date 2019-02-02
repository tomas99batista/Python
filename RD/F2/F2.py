#encoding:utf-8
#F2
#Rafael Direito

def ler_ficheiro(ficheiro):
	lista=[]
	fin= open(ficheiro)
	for lines in fin:
		lines=lines.strip()
		lista.append(lines)
	dicionario=dict()
	##print (lista[0:9])
	contador=0
	n=0
	while n < len(lista):
		lDetalhes=[]
		contador+=1
		if n == (len(lista)-1):
			n=-1
		for a in lista[n:(n+9)]:
			a = a.split(",")
			lDetalhes.append(a)
		dicionario[contador] = lDetalhes
		n+=9
	#print(dicionario)

	return(dicionario)	
	
	
def verificar(a):
	flag =True
	lista=["0","1","2","3","4","5","6","7","8","9"]	
	for x in a:
		if x not in lista:
			flag=False
	return flag
	
	
def jornadas(doc):
	
	nr=input("Jornada? ")
	dadosJornada={}
	resultados=[]
	n=0
	if verificar(nr) == False:
		return jornadas(doc)
	nr=int(nr)
	if nr not in doc.keys():
		print("Jornada sem resultados!")
		return jornadas(doc)
	elif nr in doc.keys():
		for x in dicionario[nr]:
			if x[3] == x[4]:
				resultado="X"
			elif x[3] > x[4]:
				resultado="1"
			else:
				resultado="2"
			resultados.append(resultado)
			n+=1
			print ("{:>2}{:>22}{:>3}{}{:<3}{:<16}{:<16}".format(("Jogo "+ str(n)),x[1] , x[3],"-" , x[4] , x[2], str(resultado)))
			dadosJornada[n]= [x[1] , x[3], x[4] , x[2], resultado]
			#guarda todos os valores desta jornada
		#print (dadosJornada)
		dados=resultados
		#print(dados)
		return dados,nr

		
def ler_ficheiro_apostas(ficheiro):
	contador=0
	listaNomes=[]
	listaApostas=[]
	fin= open(ficheiro)
	for lines in fin:
		contador+=1
		lines=lines.strip()
		nome, j1,j2,j3,j4,j5,j6,j7,j8,j9= lines.split(",")
		listaNomes.append(nome)
		listaApostas.append([j1,j2,j3,j4,j5,j6,j7,j8,j9])
	
	index=-1

	apostasTotal=0
	while index < (len(listaApostas)-1):
		index+=1
		A1=0
		A2=0
		A3=0
		for x in range(0,9):
			if len(listaApostas[index][x]) == 1:
				A1+=1
			elif len(listaApostas[index][x]) == 2:
				A2+=1
			elif len(listaApostas[index][x]) == 3:
				A3+=1
		contadorApostas = 1**A1*2**A2*3**A3
		apostasTotal+=contadorApostas
	#print(apostasTotal)
	#print(A1, A2, A3)
	#print(contadorApostas)	
	boletins = contador
	apostas=apostasTotal
	receitas= round(float(apostas*0.4),2)
	premios= round((0.6*receitas),2)
	
	print( "{:<20}{:>11}".format(("Num de Boletins:"),boletins))
	print( "{:<20}{:>11}".format(("Num de Apostas:"),apostas))
	print( "{:<20}{:>11}{:<10}".format(("Receita:"),receitas," euros"))
	print( "{:<20}{:>11}{:<10}".format(("Montante pŕemios:"),premios," euros"))
	
	return boletins, receitas, premios, listaApostas, listaNomes



def vencedores(dados,boletins, receitas, premios, listaApostas, listaNomes):
	iApostas=-1
	listaVencedores=[]
	while iApostas< (len(listaApostas)-1):
		iApostas+=1
		certas=0
		x=-1
		while x < (len(dados)-1):
			x+=1
			if str(dados[x]) in str(listaApostas[iApostas][x]):
				certas+=1
		listaVencedores.append(certas)
	iVencedores=-1
	primPremio=0
	segPremio=0
	terPremio=0
	while iVencedores < (len(listaVencedores)-1):
		iVencedores+=1
		if listaVencedores[iVencedores] == 9:
			primPremio+=1
		elif listaVencedores[iVencedores] == 8:
			segPremio+=1
		elif listaVencedores[iVencedores] == 7:
			terPremio+=1
	if primPremio ==0:
		valor1=0
	if primPremio !=0:
		valor1=round(((0.2*receitas)/float(primPremio)),2)
	if segPremio ==0:
		valor2=0
	if segPremio !=0:
		valor2=round(((0.2*receitas)/float(segPremio)),2)
	if terPremio ==0:
		valor3=0
	if terPremio !=0:
		valor3=round(((0.2*receitas)/float(terPremio)),2)
		
	#print(primPremio, segPremio, terPremio)
	print("{:^8}{}{:^9}{}{:^21}{}{:^17}".format("Prémio",":",("Acertos"),":",("Boletins vencedores"),":", ("Valor do Prémio")))
	print("{:^8}{}{:^9}{}{:>13}{:>9}{:>11}".format("1º",":","9",":",(primPremio),":",valor1))
	print("{:^8}{}{:^9}{}{:>13}{:>9}{:>11}".format("1º",":","8",":",(segPremio),":", valor2))
	print("{:^8}{}{:^9}{}{:>13}{:>9}{:>11}".format("1º",":","7",":",(terPremio),":", valor3))

dicionario=ler_ficheiro("Jogos.csv")
dados, nr = jornadas(dicionario)
print("")
boletins, receitas, premios, listaApostas, listaNomes=ler_ficheiro_apostas("apostas"+str(nr)+".csv")
print("")
vencedores(dados,boletins, receitas, premios, listaApostas, listaNomes)

