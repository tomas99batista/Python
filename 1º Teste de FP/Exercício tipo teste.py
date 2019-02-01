import math,sys

def decisao_1(opcao1):
    if opcao1 == 1:
        figura = "Quadrado"
    elif opcao1 == 2:
        figura = "Retângulo"
    elif opcao1 == 3:
        figura = "Triângulo"
    else:
        figura = "Círculo"
    return figura

def decisao_2(opcao2):
    if opcao2 == 5:
        grandeza = "Perímetro"
    elif opcao2 == 6:
        grandeza = "Área"
    else:
        grandeza = "Volume do sólido correspondente"
    return grandeza

def perimetroQuadrado(lado):
    perimetro = lado * 4
    return perimetro

def perimetroRetangulo(comprimento,largura):
    perimetro = comprimento * 2 + largura * 4
    return perimetro

def perimetroTriangulo(lado):
    perimetro = lado * 3
    return perimetro

def perimetroCirculo(raio):
    perimetro = 2 * math.pi * raio
    return perimetro

def areaQuadrado(lado):
    area = lado **2
    return area

def areaRetangulo(comprimento,largura):
    area = comprimento * largura
    return area

def areaTriangulo(lado):
    altura = math.sqrt((lado**2) - ((lado/2)**2))
    area = lado * altura
    return area

def areaCirculo(raio):
    area = math.pi * raio**2
    return area

def volumeCubo(lado):
    volume = lado ** 3
    return volume

def volumeRetangulo(altura):
    volume = areaRetangulo(comprimento,largura) * altura
    return volume

def volumePrisma(altura):
    volume = areaTriangulo(lado) * altura
    return volume

def volumeEsfera(raio):
    volume = (4/3) * math.pi * raio**3
    return volume

while True:
    opcao1 = int(input('''Escolha uma figura:
    (1) Quadrado
    (2) Retângulo
    (3) Triângulo
    (4) Círculo
    (0) Sair
    >>> '''))
    
    if opcao1 == 0:
        print("Saíu\n")
        sys.exit()        
    elif opcao1 < 1 or opcao1 > 4:
        print("ERRO! Tente novamente.")
    else:
        break
    
while True:
    opcao2 = int(input('''Escolha a grandeza a calcular:
    (5) Perímetro
    (6) Área
    (7) Volume do sólido correspondente
    (0) Sair
    >>> '''))
    
    if opcao2 == 0:
        print("Saíu\n")
        sys.exit() 
    elif opcao2 < 5 or opcao1 > 7:
        print("ERRO! Tente novamente.")
    else:
        break
    
while True:
    figura = decisao_1(opcao1)
    grandeza = decisao_2(opcao2)
    print("Figura: ",figura)
    print("Grandeza: ",grandeza)
    if opcao1 == 1:
        lado = float(input("Lado: "))
        if lado <= 0:
            print("ERRO! Tente novamente.")
        else:
            if opcao2 == 5:
                perimetro = perimetroQuadrado(lado)
                print("Perímetro: ",perimetro)
            elif opcao2 == 6:
                area = areaQuadrado(lado)
                print("Área: ",area)
            else:
                volume = volumeCubo(lado)
                print("Volume: ",volume)
            break
    elif opcao1 == 2:
        if opcao2 == 5 or opcao2 == 6:
            comprimento = float(input("Comprimento: "))
            largura = float(input("Largura: "))
            if comprimento <= 0 or largura <= 0:
                print("ERRO! Tente novamente.")
            else:
                if opcao2 == 5:
                    perimetro = perimetroRetangulo(comprimento,largura)
                    print("Perímetro: ",perimetro)
                elif opcao2 == 6:
                    area = areaRetangulo(comprimento,largura)
                    print("Área: ",area)
                break
        else:
            comprimento = float(input("Comprimento: "))
            largura = float(input("Largura: "))
            altura = float(input("Altura: "))
            if comprimento <= 0 or largura <= 0 or altura <= 0:
                print("ERRO! Tente novamente.")
            else:
                volume = volumeRetangulo(altura)
                print("Volume: ",volume)
                break
            
    elif opcao1 == 3:
        if opcao2 == 5 or opcao2 == 6:
            lado = float(input("Lado: "))
            if lado <= 0:
                print("ERRO! Tente novamente.")
            else:
                if opcao2 == 5:
                    perimetro = perimetroTriangulo(lado)
                    print("Perímetro: ",perimetro)
                elif opcao2 == 6:
                    area = areaTriangulo(lado)
                    print("Área: ",area)
                break
        else:
            lado = float(input("Lado: "))
            altura = float(input("Altura: "))
            if lado <= 0 or altura <= 0:
                print("ERRO! Tente novamente.")
            else:
                volume = volumePrisma(altura)
                print("Volume: ",volume)                
                break
    else:
            raio = float(input("Raio: "))
            if raio <= 0:
                print("ERRO! Tente novamente.")
            else:
                if opcao2 == 5:
                    perimetro = perimetroCirculo(raio)
                    print("Perímetro: ",perimetro)
                elif opcao2 == 6:
                    area = areaCirculo(raio)
                    print("Área: ",area)
                else:
                    volume = volumeEsfera(raio)
                    print("Volume: ",volume)
                break
                        
        
            
        
