#2015-16
#código secreto formado por N algarismos.
from random import randint

def segredo():
    codigo = ""
    for x in range (0, 4):
        codigo += str(randint(0, 9))
    return codigo

#segredo()

def valida(code):
    if len(code) != 4 or not code.isdigit():
        print("Usa 4 algarismos burro!")
        return False
    else:
        return True

#apos cada jogo mostrar pontuacao da jogada e pontuacao total acumulada
#10 pontos no sitio certo, 1 ponto por numeros iguais
#bonus 100 pontos por cada tentativa nao usada (Fazer subtracao 10 - tries)
def jogo():
    tentativa = 1
    pont_acumulada = 0
    codigo = segredo()
    print("adivinha os 4 algarismos!")
    print(codigo)
    while True:
        lugar_certas = 0
        lugar_erradas = 0
        pont_ronda = 0
        chance = input("Tentativa {tentativa}? ")
        #Retficate that the input its valid
        check_flag = True
        while check_flag == True:
            check = valida(chance)
            if check == False:
                chance = input("Tentativa {tentativa}? ")
            else:
                check_flag = False
        #Vai comparar as 2 strings agora
        for i_codigo in codigo:
            for j_chance in chance:
                print(i_codigo, j_chance)
                #2 Chars iguais
                if i_codigo == j_chance:
                    print("Olha deu igual")
                    #Se estiverem no mesmo sitio!!!
                    if codigo.index(i_codigo) == chance.index(j_chance):
                        pont_ronda += 10
                        lugar_certas += 1
                    #Se nao estiverem no mesmo sitio
                    else:
                        pont_ronda +=1
                        lugar_certas += 1
        pont_acumulada += pont_ronda
        #Se adivinhar todas acaba o jogooooooooo
        if lugar_certas == 4:
            print(lugar_certas, "certas,", lugar_erradas, "no lugar errado,", pont_ronda, "pontos, total:",pont_acumulada, "pontos")       
            restante = 10 - tentativa            
            pont_acumulada += 100*restante
            print("Conseguiste em ", tentativa, "tentativas")
            print("Total: ", pont_acumulada," pontos")
            #IR VER FICHEIRO E ESSAS MERDAS
        
        else:
            print(lugar_certas, "certas,", lugar_erradas, "no lugar errado,", pont_ronda, "pontos, total:",pont_acumulada, "pontos")            
            tentativa += 1

jogo()