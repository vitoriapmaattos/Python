"""
Escreva um programa que analise o texto abaixo e formate todos os cpf válidos
para o formato 999.999.999-99. Para o cpf ser considerado válido ele deve ser
composto de 11 dígitos. Após a formatação mostre os cpfs na tela.
"""
import re

cpfs = []

texto = """
 Ricardo, cujo CPF é 123.456789-01, reuniu-se com Ana, cujo CPF é 987654.321-10,
 para discutir sobre o projeto. Ambos discutiram sobre a proposta de Carlos, 
 que tinha o CPF 456.123.78923, mas não puderam chegar a uma conclusão. Eles 
 decidiram agendar uma nova reunião para o próximo mês. Ana disse que também 
 conversaria com seu colega João, cujo CPF é 321.65498745, para obter uma 
 perspectiva adicional. Esse é um CPF inválido: 321.123.1232-12.
 """

padrao1 = r"\d{3}.?\d{3}.?\d{3,4}-?\d{2}?"
cpfs.append(re.findall(padrao1, texto))
cpfnum = [int(cpf) for item in cpfs]

# Padrão do CPF
padrao = r"^\d{3}.?\d{3}.?\d{3}-?\d{2}$"
for cpf in cpfs:
    if not re.match(padrao, cpfs):
        print(f"O CPF {cpf} é inválido")
    else:
        # Limpando a formatação (. e -)
        cpf_limpo = re.sub(r"\D", "", cpf)

    # Verificando se os dígitos são iguais
    if cpf_limpo == cpf_limpo[0] * 11:
        print(f"O cpf {cpf} é inválido")
    else:
        # Gerando o primeiro dígito
        soma_digito1 = sum([int(digito) * i for digito, i in zip(cpf_limpo[:-2], range(10, 1, -1))])

        digito1 = 11 - (soma_digito1 % 11)
        if digito1 > 9:
            digito1 = 0

        # Comparando o primeiro dígito verificador
        cpg_gerado = f"{cpf_limpo[:-2]}{digito1}"
        if cpf_limpo[:-1] != cpg_gerado:
            print(f"O CPF {cpf} é inválido")
        else:
            # Gerando o segundo dígito
            soma_digito2 = sum([int(digito) * i for digito, i in zip(cpf_limpo[:-2] + str(digito1), range(11, 1, -1))])
            digito2 = 11 - (soma_digito2 % 11)
            if digito2 > 9:
                digito2 = 0

            # Comparando o segundo dígito verificador
            cpf_gerado = f"{cpf_limpo[:-2]}{digito1}{digito2}"

            if cpf_limpo == cpf_gerado:
                print(f"O CPF {cpf} é válido")
            else:
                print(f"O CPF {cpf} é inválido")