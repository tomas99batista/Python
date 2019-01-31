import random

def lerPalavra():
	nomeFicheiro=input("Ficheiro: ")
	fic=open(nomeFicheiro)
	wordArray=[]
	contagem=-1
	for linha in fic:
		contagem+=1
		word=linha.strip()
		wordArray.append(word)

	n=random.randint(0,contagem)
	palavra=wordArray[n].upper()
	return palavra

def escreverPalavra(letrasUsadas,palavra):
	letrasAdivinhadas=""
	for letra in palavra:
		if letra in letrasUsadas:
			letrasAdivinhadas+=letra
		else:
			letrasAdivinhadas+="-"
	return letrasAdivinhadas

def jogo():

	palavra=lerPalavra()
	letrasUsadas=[]
	tentativas=9

	while True:

		letrasAdivinhadas=escreverPalavra(letrasUsadas,palavra)

		if tentativas == 0:
			print(" "*3+"-"*7)
			print(" "*3 + "O" + " "*5 + "|")
			print(" " + "/" + " " + "|" + " " + "\ " + " "*2 + "|")
			print(" "*2 + "/" + " " + "\ " + " "*3 + "|")
			print(" "*6 + "_"*3 + "|" + "_"*3)
			print("{}".format(palavra))
			break

		elif letrasAdivinhadas == palavra:
			print("Parabéns")
			print(palavra)
			break

		else:
			guess=input("{}   {} tentativas. Próxima Letra? ".format(letrasAdivinhadas, tentativas)).upper()
			if guess not in palavra:
				letrasUsadas.append(guess)
				tentativas-=1
			elif guess in palavra:
				letrasUsadas.append(guess)

jogo()
