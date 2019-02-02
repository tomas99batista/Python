#encoding: utf-8
#F2 2015/2016
#Rafael Direito

import os
import json
import pprint

def readFile():
	ficheiro = input("Ficheiro-triagem : ")
	pacientes =  input("Ficheiro-pacientes: ")
	sin =input("Ficheiro-tempo/sintoma: ")
	if os.path.exists(ficheiro) ==  False or os.path.exists(pacientes) ==  False or os.path.exists(sin) ==  False:
		print("Erro!")
		return readFile()
	
	fin = open(ficheiro)
	cores = json.load(fin)
	
	fin2 = open(pacientes)
	pacientes = json.load(fin2)
	
	
	tempoSintoma=dict()
	
	fin3 = open(sin)
	for lines in fin3:
		linesS=lines.strip()
		sint, tempo = linesS.split(",")
		if "h" in tempo:
			hora, minuto = tempo.split("h")
			if "00" not in minuto:
				minuto, nada = minuto.split("m")
			else:
				minuto=0
		else:
			hora=0
			minuto,nada=tempo.split("m")
		x= 60*int(hora) + int(minuto)
		#print(x)
		tempoSintoma[sint]=x

	triagem=dict()
	for kCores in cores:
		for sintomas in cores[kCores]:
			for kPacientes in pacientes:
				if sintomas in pacientes[kPacientes]:
					triagem[kPacientes]=kCores
	print("TRIAGEM----------------------------------------------")
	for a in triagem.keys():
		print ("{} {} {:<10}".format(str(a)+": ", "-->", triagem[a]))

	return triagem,tempoSintoma,pacientes
	



def ordenar(dic):
	
	azul,verde,amarelo,laranja,vermelho = [],[],[],[],[]
	for nomes in dic.keys():
		if dic[nomes] == "Vermelho":
			vermelho.append(nomes)
		elif dic[nomes] == "Laranja":
			laranja.append(nomes)
		elif dic[nomes] == "Amarelo":
			amarelo.append(nomes)
		elif dic[nomes] == "Verde":
			verde.append(nomes)
		else:
			azul.append(nomes)
	triagemCor={}
	triagemOrdenada = vermelho+laranja+amarelo+verde+azul
	triagemCor["Vermelho"] = vermelho
	triagemCor["Laranja"] = laranja
	triagemCor["Amarelo"] = amarelo
	triagemCor["Verde"] = verde
	triagemCor["Azul"] = azul
	print("")
	print("ORDEM DE ATENDIMENTOS----------------------------------------------")
	n=0
	for x in triagemOrdenada:
		n+=1
		print("{:<5} {:<22}".format(str(n)+"º:", x))
	return triagemOrdenada, triagemCor
		
		
		
		
def tempo_espera(pacientes,tempo):
	tEspera={}
	for pessoas in pacientes.keys():
		for t in tempo.keys():
			if t in pacientes[pessoas]:
				tEspera[pessoas] = tempo[t]
	return tEspera
		
		
		
def stats(pacientes,tempo, cor):
	tempos=0
	porCor={}
	tCor=[]
	print("")
	print("TEMPO DE ESPERA POR PACIENTE----------------------------------------------")
	for nomes in pacientes:
		for t in tempo.keys():
			if nomes in t:
				print("{:<18} {:>8} {}". format(str(nomes)+" :", str(tempos),"min"))
				tCor.append(tempos)
				tempos+= tempo[t]
	media={}
	inicio =0
	fim = ((len(cor["Vermelho"])))
	tVermelho = tCor[inicio:fim]
	media["Vermelho"] = tVermelho , len(tVermelho)
	inicio= fim
	fim = fim+((len(cor["Laranja"])))
	tLaranja = tCor[inicio:fim]
	media["Laranja"] = tLaranja , len(tLaranja)
	inicio= fim
	fim = fim+((len(cor["Amarelo"])))
	tAmarelo = tCor[inicio:fim]
	media["Amarelo"] = tAmarelo , len(tAmarelo)
	inicio= fim
	fim = fim+((len(cor["Verde"])))
	tVerde = tCor[inicio:fim]
	media["Verde"] = tVerde , len(tVerde)
	inicio= fim
	fim = fim+((len(cor["Azul"])))
	tAzul = tCor[inicio:fim]
	media["Azul"] = tAzul , len(tAzul)
	
	final={}
	for keys in media.keys():
		m = round(((sum(media[keys][0]))/media[keys][1]),2)
		final[keys]=m
		
		
	listaM=[]
	for val in final.values():
		listaM.append(val)
	
	
	mediasOrdenadas = ordenar1(listaM)
	print("")
	print("TEMPOS MÉDIOS POR COR----------------------------------------------")
	for m in mediasOrdenadas:
		for k in final.keys():
			if  m==final[k]:
				print("{:<12} {:<8}".format(k+" :",final[k]))
		
	#print(final)


def ordenar1(lista):
	if len(lista)<=1:
		return lista
	pivot = lista[0]
	antes=[p for p in lista[1:] if p < pivot]
	depois=[n for n in lista[1:] if n >=pivot]
	
	return ordenar1(antes)+[pivot]+ordenar1(depois)
	
	
	
		
triagem, tempos,pacientes =readFile()
triagemOrdenada, triagemCor =ordenar(triagem)
tEspera = tempo_espera(pacientes,tempos)	
stats(triagemOrdenada, tEspera,triagemCor)
