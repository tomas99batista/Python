#Eleitores

def boletim():
    print("1 - Democratas\n2 - Republicanos\n3 - Liberais\n0 - Branco")
    voto = int(input("Digite o nº correspondente ao seu voto: "))
    while voto != 1 and voto != 2 and voto != 3 and voto != 0 and not voto.isnumeric(): 
        print("ERRO! Opcao nao disponivel")
        voto = int(input("Digite o nº correspondente ao seu voto: "))
    return voto
#---------------------------------------------------------
def ler_caderno(num):
    caderno = open("caderno.txt", "r")
    flag_found = 0
    for line in caderno:
        linha = line.split(",")
        numero_eleitor = linha[0]
        if numero_eleitor == num:
            flag_found = 1
    if flag_found == 1:
        return True
    else:
        return False
#---------------------------------------------------------

def mesa_voto():
    democratas_votos = 0
    republicanos_votos = 0
    liberais_votos = 0
    brancos_votos = 0
    totais_votos = 0
    end_flag = 0
    print("Bem vindo as eleicoes")
    while end_flag == 0:
        numero_eleitor = input("Pfv insira o seu numero de eleitor: ")
        if ler_caderno(numero_eleitor) == True:
            voto = boletim()
            print("Voto aceite.")
            if voto == 1:
                democratas_votos += 1
                totais_votos += 1
            elif voto == 2:
                republicanos_votos += 1
                totais_votos += 1
            elif voto == 3:
                liberais_votos += 1
                totais_votos += 1
            elif voto == 0:
                brancos_votos += 1
                totais_votos += 1
        elif numero_eleitor.upper() == "FIM":
            end_flag = 1
        elif ler_caderno(numero_eleitor) == False:
            print("Pedimos desculpa o seu nome nao consta nos cadernos eleitorais")
    print("------------MESAS_ENCERRADAS------------")
    votos_percentagem = totais_votos - brancos_votos
    democratas_percentagem = (democratas_votos/votos_percentagem) * 100
    republicanos_percentagem = (republicanos_votos/votos_percentagem) * 100
    abstencao_total = votadores_total-totais_votos
    abstencao_percentagem = (abstencao_total/votadores_total) * 100
    print("Democratas:", democratas_votos, "votos (", democratas_percentagem, "%)")
    print("Republicanos:", republicanos_votos, "votos (", republicanos_percentagem, "%)")
    print("Brancos:", brancos_votos, "votos")
    print("Abstenção:", abstencao_total, "(", abstencao_percentagem, "%)")
#---------------------------------------------------------
votadores_total = 0
caderno = open("caderno.txt", "r")
for line in caderno:
    votadores_total += 1
    
mesa_voto()