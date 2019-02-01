#Nome: Tiago Carvalho Mendes Nº Mec: 88886

def IMC(peso,altura): #Esta função calcula o índice de massa corporal de uma pessoa
    imc = peso / (altura**2)
    imc = round(imc, 1)
    return imc

def classificacao(imc): #Esta função classifica o índice de massa corporal de uma pessoa
    if imc < 18.5:
        print("O adulto tem um IMC de",imc,"\nBaixo Peso")
    elif 18.5 <= imc <= 25:
        print("O adulto tem um IMC de",imc,"\nNormal")
    else:
        print("O adulto tem um IMC de",imc,"\nObesidade")
        
def lerValorRealPositivo(grandeza): #Esta função averigua se os valores das grandezas peso e altura são número reais positivos
    if grandeza == 1:
        grandeza = float(input("Peso?(kg) "))
        while grandeza <= 0:
            grandeza = float(input("Número inválido! Peso?(kg) "))
    elif grandeza == 2:
        grandeza = float(input("Altura?(m) "))
        while grandeza <= 0:
            grandeza = float(input("Número inválido! Altura?(m) "))
    return grandeza

def menu(): #Esta função apresenta um menu de interação com o utilizador
    count = 0
    soma = 0
    while True:
        n = eval(input("Opções disponíveis:\n0 - sair\n1 - introduzir nova medida\n2 - mostrar média atual\nOpção? "))
        if n < 0 or n > 2 or type(n) != int:
            print("Opção inválida!")
        else:
            if n == 2 and count == 0:
                print("Estatísticas atuais:\nAinda não foram introduzidos cálculos!")
            elif n == 1:
                grandeza = 1
                peso = lerValorRealPositivo(grandeza)
                grandeza = 2
                altura = lerValorRealPositivo(grandeza)
                imc = IMC(peso,altura)
                classificacao(imc)
                count += 1
                soma += imc
            elif n == 2 and count != 0:
                print("Estatísticas atuais:\nValor médio do IMC para",count,"adultos: ",round((soma / count), 1))
            else:
                print("FIM\nAté breve")
                break
                
print("CALCULADORA DO ÍNDICE DE MASSA CORPORAL")             
menu() #Ao chamar aqui a função, ela executará todo o meu programa
                
            
            
    
        
    
