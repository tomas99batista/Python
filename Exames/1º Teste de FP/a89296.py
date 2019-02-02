#IMC Calculator with peso & altura given by the user
print("Hello, bem vindo a calculadora do IMC, pfv insira peso e altura")
peso = int(input("Peso? (kg): "))
altura = float(input("Altura? (m): "))
IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Baixo Peso! IMC:", IMC)
elif 18.5 <= IMC <= 25:
    print("Normal! IMC:", IMC)
elif IMC > 25:
    print("Peso ALTO! IMC:", IMC)

print("FIM!")