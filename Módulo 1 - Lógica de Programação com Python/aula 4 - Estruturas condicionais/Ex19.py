"""
Faça um algoritmo que calcule o peso de uma pessoa em outros planetas.
Para isso o programa deve solicitar o peso da pessoa, em qual planeta
ela deseja saber o seu peso e utilizar a seguinte escala de gravidade
dos planetas em relação a terra
"""

peso = float(input("Qual o seu peso? "))
planeta = input("Qual planeta deseja saber o peso? ")mjoadcvhipidhoep´fsjoadvp

match planeta:
    case "Mercúrio":
        print(f"O peso no planeta será {peso * 0.38}")
    case "Vênus":
        print(f"O peso no planeta será {peso * 0.91}")
    case "Marte":
        print(f"O peso no planeta será {peso * 0.38}")
    case "Jupter":
        print(f"O peso no planeta será {peso * 2.34}")
    case "Saturno":
        print(f"O peso no planeta será {peso * 0.93}")
    case "Urano":
        print(f"O peso no planeta será {peso * 0.92}")
    case "Netuno":
        print(f"O peso no planeta será {(peso * 1.12):.2f}")
    case "Plutão":
        print(f"O peso no planeta será {peso * 0.06}")
    case _:
        print("Planeta inválido")
