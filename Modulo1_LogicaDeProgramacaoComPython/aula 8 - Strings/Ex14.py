"""
Faça um algoritmo que receba um número de telefone no formato:
+99 (99) 9 9999-9999. Caso o número recebido não seja válido ele deve
informar o usuário que o número é inválido; caso contrário o programa deve
mostrar apenas os números do telefone no formato 9999999999999.
"""
import re

telefone = input("Digite um número de telefone: ")
padrao = r"^\+\d{2} \(\d{2}\) 9 \d{4}-\d{4}$"

if re.match(padrao, telefone):
    telefone = re.sub(r"\D", "", telefone)
    print(telefone)
else:
    print("Telefone inválido")