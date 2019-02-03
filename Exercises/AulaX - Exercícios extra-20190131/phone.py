def menu():
    print("1 - Registar chamada\n2 - Ler ficheiro\n3 - Listar clientes\n4 - Fatura\n5 - Terminar")

def validation(phone_number):
    #se tiver menos de 3 numeros
    if len(phone_number.isnumeric()) < 3:
        return True

    #se nao comecar por + ou por um numero
    if not phone_number[0] == "+" or not phone_number[0].isnumeric():
        return True
  
    #se comecar por + e para a frente tiver nao numeros
    if phone_number[0] == "+" or not phone_number[1:].isnumeric():
        return True
    
    return False

def register_call():
    while True:
        origem = input("Telefone origem? ")
        validation(origem)
    
    while True:
        destino = input("Telefone destino? ")
        validation(destino)
    
    while True:
        duracao = input("Duracao? (s) ")            
        validation(duracao)

register_call()
