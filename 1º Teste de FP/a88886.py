#Nome: Tiago Carvalho Mendes Nº Mec: 88886

peso = float(input("Peso (kg)? "))
altura = float(input("Altura (m)? "))

imc = peso / (altura**2)

if imc < 18.5:
    print("O adulto tem um IMC de",imc,"\nBaixo Peso")
elif 18.5 <= imc <= 25:
    print("O adulto tem um IMC de",imc,"\nNormal")
else:
    print("O adulto tem um IMC de",imc,"\nObesidade")
