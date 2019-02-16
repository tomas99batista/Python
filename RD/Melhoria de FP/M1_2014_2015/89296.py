#Blackjack
#2,3,4,5,6,7, Dama (8), Valete(9), Rei (10), Ás (11)
from random import randint

#this function will convert the card name to a value
def converter(card_name):
    if card_name.upper() == "DAMA":
        valor = 8
        return valor
    elif card_name.upper() == "VALETE":
        valor = 9
        return valor
    elif card_name.upper() == "REI":
        valor = 10
        return valor
    elif card_name.upper() == "AS":
        valor = 11
        return valor
    valor = int(card_name)
    return valor

def pontuacao(pont_dealer, pont_jogador):
    #Se o dealer passa os 21
    if pont_dealer > 21:
        return 1
    #Se o jogador passa os 21
    elif pont_jogador > 21:
        return 0
    #Empate ganha a casa!
    elif pont_dealer == pont_jogador:
        return 0  
    #Dealer fez 21
    elif pont_dealer == 21:
        return 0
    #Jog. fez 21
    elif pont_jogador == 21:
        return 1
    #Se o dealer ganha   
    elif pont_dealer > pont_jogador:
        return 0 
    #Se o jogador ganha
    elif pont_dealer < pont_jogador:
        return 1  
#--------------------------------------------------------------------

#Utilizando as funções anteriores, crie uma
#versão simplificada do jogo em que os jogadores apenas
#têm as duas cartas iniciais. Mostre a pontuação de cada
#um e qual o vencedor.
def jogo():
    dealer_win = 0
    jogador_win = 0
    jogo = 1
    jogar = 1
    while jogar == 1:
        if jogar == 1:
            carta1_dealer = randint(2,11)
            carta2_dealer = randint(2,11)
            carta1_player = randint(2,11)
            carta2_player = randint(2,11) 
            soma_dealer = carta1_dealer + carta2_dealer
            soma_jogador = carta1_player + carta2_player
            choice = 1
            print("\nJOGADOR: Points: ", soma_jogador, " Cartas: ", carta1_player, carta2_player)
            while soma_jogador <= 21 and choice != 0:
                choice = int(input("Jogador, deseja mais cartas? 1-SIM | 0-NAO "))
                if choice == 1:
                    carta_nova_player = randint(2,11) 
                    soma_jogador += carta_nova_player
                    print("JOGADOR: Points: ", soma_jogador, " Cartas: ", carta1_player, carta2_player, carta_nova_player)

            points = pontuacao(soma_dealer, soma_jogador)
            #Dealer ganhou
            #AQUI ARMAZENA QUEM GANHOU COM QUANTOS PONTOS NUM FILE
            #Jogo X: D/J Ganhou com X pontos. Vitorias = Dealer X - Y Jogador
            file_registo = open("registo.txt", "w")
            #Dealer ganha
            if points == 0:
                print("\nDealer GANHA!!! Pontuacao:", soma_dealer)
                print("Jogador perde. Pontuacao:", soma_jogador)
                dealer_win += 1
                file_registo.write("Jogo {jogo}: Dealer ganhou com {soma_dealer}. Vitorias = DEALER {dealer_win} - {jogador_win} JOGADOR")
            #Jogador ganha
            elif points == 1:
                print("\nJogador GANHA!!! Pontuacao:", soma_jogador)
                print("Dealer perde. Pontuacao:", soma_dealer)
                jogador_win += 1
                file_registo.write("Jogo {jogo}: Jogador ganhou com {soma_jogador}. Vitorias = DEALER {dealer_win} - {jogador_win} JOGADOR")
            jogar = int(input("\n##################\nQuer jogar mais? 1 - SIM | 0 - NAO "))
            #Aumenta o num dos jogos
            jogo += 1
        else:
            print("Obrigado por ter jogado! RESULTADOS: ")
jogo()