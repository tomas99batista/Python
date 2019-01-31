#encoding:utf-8
#M2 2015/2016
#Rafael Direito

#imports

import os

#código

def readFile():
	ficheiro ="weather.csv"#input("Ficheiro-sensores: ")
	
	if os.path.exists(ficheiro) == False:
		print("O ficheiro nao existe!")
		return readFile()
	
	fin = open(ficheiro)
	dados= dict()
	valores=[]
	media=dict()
	for lines in fin:
		
		datasA=[]
		datas=[]
		line = lines.strip()
		sensor,data,valor = line.split(",")
		dataA, ignorar = data.split("T")
		datas.append(data)
		datasA.append(dataA)
		valores.append(float(valor))
		if sensor not in dados:
			dados[sensor]={}
		dados[sensor][valor]=(data,dataA)		
	return dados



def min_max(dicionario):
	mM={}
	for k in dicionario.keys():
		minimo = min(dicionario[k].keys())
		maximo= max(dicionario[k].keys())
		mM[k]=(maximo, dicionario[k][maximo][0]),(minimo, dicionario[k][minimo][0])
	
		print(k+":")
		print("{:<8}{} {} {} {}".format("","Minimo:",str(minimo) ,"a",str(dicionario[k][minimo][0])))
		print("{:<8}{} {} {} {}".format("","Maximo:",str(maximo) ,"a",str(dicionario[k][maximo][0])))



def media(dicionario):
	listaDias=[]
	for k in dicionario.keys():
		for v in dicionario[k]:
			d= dicionario[k][v][1]
			if d not in listaDias:
				listaDias.append(d)
	#print(listaDias) --------------- tem os os dias em que houve registos
	
	#print(listaDias)
	datas=[]
	valorData= {}
	for k in dicionario.keys():
		for v in dicionario[k]:
			datas.append([dicionario[k][v][1],v])	
		valorData[k]=datas
		
	#print(valorData)------------------dicionario com os dias e o valor
	#print(valorData["Temperature"])
	return valorData
	
def media_diaria(lista):
	dataValor={}
	for tuplos in lista:
		if tuplos[0] not in dataValor:
			dataValor[tuplos[0]]=[]
		dataValor[tuplos[0]].append(tuplos[1])
	print(dataValor)
	
		
		
		
dados=readFile()
#min_max(dados)
valorData=media(dados)	
media_diaria(valorData["Temperature"])
