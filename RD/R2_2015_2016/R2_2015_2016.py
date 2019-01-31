#encoding:utf-8
#R2 2015/2016
#Rafael Direito
import os
import random

def lerFicheiro():
	doc = input("Ficheiro a ler: ")
	if os.path.exists(doc):
		fin = open(doc)
		return fin
	else:
		return lerFicheiro()

def manipularFicheiro(doc):
	geral=dict()
	apostas=[]
	for lines in doc:
		linesS=lines.strip()
		nome, cidade, aposta = linesS.split(",")
		apostas=aposta.split()
		geral[nome]=[cidade,apostas]
	print(len(geral))
	return geral

def sorteio():
	chave=[]
	for x in range(4):
		a=random.randint(1,20)
		a=str(a)
		if len(a) ==1:
			a=("0"+a)
		if str(a) not in chave:
			chave.append(str(a))
	if len(chave) != 4:
		return sorteio()
	chave =ordenar(chave)
	print("Chave Sorteada:  {}  {}  {}  {}".format(chave[0],chave[1],chave[2],chave[3]))
	return chave


def ordenar(lista):
	if len(lista) <=1:
		return lista
	pivot=lista[0]
	antes = [p for p in lista[1:] if p < pivot]
	depois= [n for n in lista[1:] if n >= pivot]
	return ordenar(antes)+[pivot]+ordenar(depois)

def certos(solucao, jogador):
	apostas=[]
	corretos=[]
	apostador=[]
	acertos=dict()
	for a in jogador.values():
		opcoes =a[1]
		apostas.append(opcoes)
	#print(apostas)
	index =-1
	while index < (len(apostas)-1):
		index+=1
		certo = 0
		for i in apostas[index]:
			if i in solucao:
				certo+=1
		corretos.append(str(certo))
	for b in jogador.keys():
		apostador.append(b)
	acertos= dict(zip(apostador,corretos))
	c4=dict()
	c3=dict()
	c2=dict()
	c1=dict()
	c0=dict()
	for pessoa in acertos.keys():
		if acertos[pessoa] == "4":
			c4[pessoa] =acertos[pessoa]
		elif acertos[pessoa] == "3":
			c3[pessoa] =acertos[pessoa]
		elif acertos[pessoa] == "2":
			c2[pessoa] =acertos[pessoa]
		elif acertos[pessoa] == "1":
			c1[pessoa] =acertos[pessoa]
		else:
			c0[pessoa] =acertos[pessoa]
	
	if len(c4) != 0 :
		print("")
		print("Primeiro Prémio: ")
		imprimirCertos(c4,geral)
	if len(c3) != 0 :
		print("")
		print("Segundo Prémio: ")
		imprimirCertos(c3,geral)
	return c4,c3,c2,c1,acertos

def receita(c4,c3,c2,c1,acertos,geral):
	receita = float(len(geral))
	v1,v2,v3,v4 =0,0,0,0
	i1,i2,i3,i4 = 0,0,0,0
	if len(c4) !=0:
		v4 = round(0.3*receita,2)
		i4=round((v4/len(c4)),2)
		
	if len(c3) !=0:
		v3 = round(0.2*receita,2)
		i3=round((v3/len(c3)),2)
	if len(c2) !=0:
		v2 = round(0.1*receita,0)
		i2=round((v2/len(c2)),2)
	if len(c1) !=0:
		v1 = round(0.1*receita,0)
		i1=round((v1/len(c1)),2)
	
	print("Receita: "+str(receita)+ " Euros")
	print("{:<12}{:>10}{:>14}{:>10}".format("Premio","Montante","Premiados","Valor"))
	print("")
	print("{:<12}{:>10}{:>14}{:>10}".format("1º premio",str(v4),str(len(c4)),str(i4)))
	print("{:<12}{:>10}{:>14}{:>10}".format("2º premio",str(v3),str(len(c3)),str(i3)))
	print("{:<12}{:>10}{:>14}{:>10}".format("3º premio",str(v2),str(len(c2)),str(i2)))
	print("{:<12}{:>10}{:>14}{:>10}".format("4º premio",str(v1),str(len(c1)),str(i1)))
	
##################################################################################33
##########################################
###########################################
##########################################
###########################################
###########################################
	
def imprimirCertos(dic,geral):	
	print("{:<20}{:<20}{:<20}".format("Pessoa", "Distrito", "Chave"))
	print("")
	for k in dic.keys():
		print("{:<20}{:<20} {}  {}  {}  {}".format(str(k), str(geral[k][0]), str(geral[k][1][0]), str(geral[k][1][1]),str(geral[k][1][2]),str(geral[k][1][3])))
	print("")
fin = lerFicheiro()
geral = manipularFicheiro(fin)
chave=sorteio()
c4,c3,c2,c1,acertos=certos(chave,geral)
receita(c4,c3,c2,c1,acertos,geral)
