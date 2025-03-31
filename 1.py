import os 
os.system("cls || clear")


soma = 0
codigos = " "

while True:
    print("""\tcodigo        \tprato             \tvalor    
            1           Picanha                 R$ 40,00
            2           Strogonoff              R$ 30,00
            3           Macarronada             R$ 25,00
            4           lasanha                 R$ 20,00
            5           Cozido de Frango        R$ 18,00
            6           Bife à Parmegiana       R$ 15,00
            7           Fígado acebolado        R$ 10,00              
          """)

    pedido = str(input("Informe o número do seu pedido: "))
        
    match pedido:
        case 1:
            escolha = "Picanha "
            codigos += 1 + " "
            preco = 40
            print(f"Prato escolhido: {escolha}")
        case 2:
            escolha = "Strogonoff"
            codigos += 1 + " "
            preco = 30
            print(f"Prato escolhido: {escolha}")
        case 3:
            escolha = "Macarronada"
            codigos += 1 + " "
            preco = 25
            print(f"Prato escolhido: {escolha}")
        case 4:
            escolha = "lasanha"
            codigos += 1 + " "
            preco = 20
            print(f"Prato escolhido: {escolha}")
        case 5:
            escolha = "cozido de frango" 
            codigos += 1 + " "
            preco = 18
            print(f"Prato escolhido: {escolha}")
        case 6:
            escolha = "Bife à Parmegiana"
            codigos += 1 + " "
            preco = 15
            print(f"Prato escolhido: {escolha}")
        case 7:
            escolha = "Fígado acebolado"
            codigos += 1 +" "
            preco = 10
            print(f"Prato escolhido: {escolha}")
        case 0:
            codigos += pedido + " "
            print("==PROGRAMA ENCERRADO==")
            break
        
        case _:
            escolha = "Opção inválida."
            preco = 0 
        
    
    soma += preco 
    continuar = (input(f"Deseja mais algum item ? \nDigite 'S' ou 'N': ")).lower()
    codigos += escolha 
    if continuar == "n":
        break
        
print (f"Pratos escolhidos: {codigos}")
print (f"")
