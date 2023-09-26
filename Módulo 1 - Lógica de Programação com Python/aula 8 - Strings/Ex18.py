"""
Refaça a questão anterior validando se o cpf é válido através do dígito
verificador. O algoritmo para fazer essa validação está descrito aqui:

https://www.macoratti.net/alg_cpf.htm#:~:text=O%20algoritmo%20de%20valida%C3%A7%C3%A3o%20do,%3A%20111.444.777%2D05.
"""

import re

cpf = input("Digite um cpf: ")

# Padrão do CPF
padrao = r"^\d{3}.?\d{3}.?\d{3}-?\d{2}$"

if not re.match(padrao, cpf):
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