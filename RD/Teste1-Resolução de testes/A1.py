#encoding:utf8

n=int(input("Escolhe um número inteiro entre 0 e 20: "))
if n < 0 or n > 20:
	print(" ERRO!!! O número selecionado não se encontra no intervalo aceite!")
if n >= 0 and n <= 20:
	for r in range(1, 101):
		print (r * (""))
	c=1
	t=int(input("Tentativa {} : Escolhe um número: ".format(c)))
	if n ==t:
		print("Foi necessária : 1 Tentativa")
	if t != n:
		t2=2000
		d=t-n
		while t2 != n:
			c+=1
			t2=int(input("Tentativa {} : Escolhe outro número: ".format(c)))
			d2=t2-n
			if d2 < 0:
				d2=d2*(-1)
			if d < 0:
				d=d*(-1)
			if d2 == d:
				print("Estás à mesma distância!")
				d=d2
			if d2 < d:
				d=d2
				print("Estás mais próximo!")
			if d2 > d:
				print ("Estás mais longe!")
				d=d2
		print("Foram necessárias : {} tentativas!".format(c))	
				

			
