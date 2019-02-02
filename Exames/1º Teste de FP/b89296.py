#Calculates the IMC and returns it given the peso and altura passed by argument
def IMC(peso, altura):
    IMC = round(peso / (altura * altura), 1)
    return IMC

def classificacao(IMC):
    if IMC < 18.5:
        print("Baixo Peso! IMC:", IMC, "\n")
    elif 18.5 <= IMC <= 25:
        print("Normal! IMC:", IMC, "\n")
    elif IMC > 25:
        print("Peso ALTO! IMC:", IMC, "\n")

#flag specifies if we want peso or altura
#flag = 1 peso; flag = 2 altura
def lerValorRealPositivo(flag):
    if flag == 1:
        peso = int(input("Peso? (kg) "))
        while peso <= 0:
            print("Insira um peso valido!")
            peso = int(input("Peso? (kg) "))
        return peso
    if flag == 2:
            altura = float(input("Altura? (m) "))
            while altura <= 0:
                print("Insira uma altura valido!")
                altura = float(input("Altura? (m) "))            
            return altura
   

def menu():
    soma = 0
    tries = 0
    while True:
        print("Opcoes:\n0 - Sair\n1 - introduzir nova medida\n2 - mostrar média atual")
        option = int(input("Option? "))
        if option < 0 or option > 2 or type(option)!= int:
            print("Opcao invalida!")
        else:
            if option == 0:
                print("FIM")
                break
            
            elif option == 1:
                peso = lerValorRealPositivo(1)
                altura = lerValorRealPositivo(2)
                imc = IMC(peso, altura)
                soma += imc
                tries += 1
                classificacao(imc)
            
            elif option == 2:
                print("Estatisticas atuais")
                if tries == 0:
                    print("Ainda nao foram feitos calculos!\n")
                else:
                    medium = round(soma/tries, 1)
                    print("Valor medio do IMC para ", tries," adultos: ", medium)
menu()