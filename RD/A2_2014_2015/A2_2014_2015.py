#encoding:utf-8
#A2- 2014/2015
#Rafael Direito

import os
import datetime


codigos=[]

def readFile():
	ficheiro =input("Ficheiro a ler: ")
	if os.path.exists(ficheiro) == False:
		print("O Ficheiro Não Existe!")
		return readFile()
	fin = open(ficheiro)
	return fin

def manipularFile(ficheiro):
	produtos=dict()
	for lines in ficheiro:
		linesS=lines.strip()
		codigo, nome,categoria,preco,iva = linesS.split(";")
		if codigo not in produtos.keys():
			produtos[codigo] = [nome,categoria,preco,iva]
	return produtos

def options(produtos):
	opcao = "x"

	while opcao != "S":
		print("CAIXA REGISTADORA")
		print("(I) Inserir produto")
		print("(F) Faturar")
		print("(S) Sair")
		opc=input(">")
		opcao=opc.upper()

		if opcao not in ["I","F","S"]:
			print("")
			print("Opção Inválida!!!")
			print("")
			return options()

		elif opcao == "I":
			inserir(produtos)

		elif opcao == "F":
			tBruto, codigos = faturar(produtos)
			
	if opcao =="S":
		registar(codigos,tBruto)

def inserir(dicionario):
	c="x"
	print("Para sair --> código: 0")
	c=str(input("Código: "))
	while c != "0" :
		if c in str(dicionario.keys()):
			codigos.append(c)
			print(dicionario[c][0] +" => "+ dicionario[c][2]+" Euros")
		else:
			print("Invalido")
		c=str(input("Código: "))


def faturar(dicionario):
	cat=dict()
	lista=[]
	listaCat=[]
	
	for cod in codigos:
		if cod in dicionario.keys():
			lista.append(dicionario[cod][0:4])
		if cod in dicionario.keys() and dicionario[cod][1] not in listaCat:
			listaCat.append(dicionario[cod][1])
	for chaves in listaCat:
		listaAdd=[]
		for valores in lista:
			if chaves in valores:
				listaAdd.append([valores[0],valores[2],valores[3]])
			cat[chaves] = listaAdd
	chaves = []
	for a in cat.keys():
		chaves.append(a)
	n=-1 
	tBruto=0
	tIVA=0
	print("")
	while n < (len(chaves)-1):
		n+=1
		print(chaves[n]+":")
		cont=0
		for b in cat[chaves[n]]:
			cont+=1
			print("{:>8} {:<26}{:<6}".format(cont,b[0]+""+" (IVA"+b[2]+") ", b[1]+" Euros"))
			tBruto+=float(b[1])
			tIVA+=float(b[1])*(float(b[2].replace("%",""))/100)
		print("")
	tBruto=round(tBruto,2)
	tIVA=round(tIVA,2)
	print("{:<20}{:>10}{}".format("Total Bruto",tBruto , " Euros"))
	print("{:<20}{:>10}{}".format("Total IVA",tIVA," Euros"))
	print("{:<20}{:>10}{}".format("Total Líquido",tBruto+tIVA," Euros"))
	print("")
	#print(codigos)
	return tBruto, codigos
	
def registar(codigo,valor):
	now = datetime.datetime.now()
	now=str(now)
	vendas = open("Vendas.txt","a")
	vendas.write(now + "   "+str(valor)+" Euros"+"\n")
	vendas.close()
	#falta ATUALIZAR STOCK
	
	
	
		
def main():
	fin = readFile()
	produtos = manipularFile(fin)
	opcao = options(produtos)
	
	
main()
