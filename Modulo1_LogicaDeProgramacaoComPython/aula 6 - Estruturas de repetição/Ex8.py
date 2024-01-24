"""
Um restaurante de fast-food oferece um menu com 4 opções de hambúrgueres:
X-Burger, X-Salada, X-Bacon e X-Tudo.
Cada hambúrguer tem um preço diferente: R$10, R$12, R$15 e R$18,
respectivamente. Escreva um programa que solicite ao usuário a quantidade
desejada de cada hambúrguer e exiba o valor total do pedido.
"""


#variáveis contadoras
burguer = 0
salada = 0
bacon = 0
tudo = 0

#constantes
valorburguer = 10
valorsalada = 12
valorbacon = 15
valortudo = 18

valortotal = 0

while True:
    pedido = input(f"""
Faça o seu pedido:

1) X-Burguer
2) X-Salada
3) X-Bancon
4) X-Tudo
0) Finalizar pedido

Total do Pedido: R$ {valortotal:.2f}

Digite a opção escolhida:
""")

    match pedido:
        case "1":
            burguer += int(input("Digite a quantidade de x-burguers: "))
            valortotal += burguer * valorburguer
        case "2":
            salada += int(input("Digite a quantidade de x-saladas: "))
            valortotal += salada * valorsalada
        case "3":
            bacon += int(input("Digite a quantidade de x-bacons: "))
            valortotal += bacon * valorbacon
        case "4":
            tudo += int(input("Digite a quantidade de x-tudos: "))
            valortotal += tudo * valortudo
        case "0":
            break
        case _:
            print("Opção inválida")

print(f"""
Pedido finalizado!

Detalhamento do pedido:
1) X-Burguer: {burguer}
2) X-Salada: {salada}
3) X-Bancon: {bacon}
4) X-Tudo: {tudo}

Total do Pedido: R$ {valortotal:.2f}
""")