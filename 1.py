import os 
os.system("cls || clear")

junta_pratos = ""
total = 0
desconto = 0
preco = 0
valor_a_pagar = 0

while True:
    print(f"""\tcodigo        \tprato             \tvalor    
            1           Picanha                 R$ 40,00
            2           Strogonoff              R$ 30,00
            3           Macarronada             R$ 25,00
            4           lasanha                 R$ 20,00
            5           Cozido de Frango        R$ 18,00
            6           Bife à Parmegiana       R$ 15,00
            7           Fígado acebolado        R$ 10,00              
            0           FECHAR O CARDÁPIO      
          """)

    pedido = int(input("Informe o número do seu pedido: "))
        
    match pedido:
        
        case 1:
            print(f"Prato escolhido: Picanha")
            preco = 40
            prato = "Picanha (#1)"
        case 2:
            print(f"Prato escolhido: Strogonoff")
            preco = 30
            prato = "Strogonoff (#2)" 
        case 3:
            print(f"Prato escolhido: Macarronada")
            preco = 25
            prato = "Macarronada (#3)"
        case 4:
            print(f"Prato escolhido: Lasanha")
            preco = 20
            prato = "Lasanha (#4)"
        case 5:
            print(f"Prato escolhido: Cozido de frango")
            preco = 18
            prato = "Cozido de frango (#5)"
        case 6:
            print(f"Prato escolhido: Bife à parmegiana")
            preco = 15
            prato = "Bife à parmegiana (#6)"
        case 7:
            print(f"Prato escolhido: Fígado acebolado")
            preco = 10
            prato = "Fígado acebolado (#7)"
        case 0:
                forma_de_pagamento = int(input("""Digite a forma de pagamento:  
                1   |   À VISTA
                2   |   À PRAZO                                               
                """))
                
                if forma_de_pagamento == 1:
                    desconto += total * 0.10
                    valor_a_pagar = total - desconto  

                    print("Forma de pagamento escolhida: À vista")
                    print(f"Valor do desconto: {desconto: .2f}")
                elif forma_de_pagamento == 2:
                    valor_a_pagar = total * 1.10
                    acrescimo = valor_a_pagar - total

                    print("Forma de pagamento escolhida: à prazo")
                    print(f"O valor do acrescimo é: {acrescimo}")
                    print(f"Valor a pagar: {valor_a_pagar: .2f}")
                    break
        case _:
            escolha = print("Opção inválida.")
 
    continuar = (input(f"Deseja mais algum item ? \nDigite 's' para continuar e/ou adicionar outro prato, ou n para finalizar a compra: ")).lower()
    junta_pratos += prato + ", "
    total += preco
    print(f"Valor à pagar: {valor_a_pagar}")
    if continuar != "s":
        break
   
