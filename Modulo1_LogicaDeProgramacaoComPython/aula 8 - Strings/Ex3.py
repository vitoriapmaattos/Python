"""
Faça um programa para anonimizar o nome completo de uma pessoa ao substituir
o último sobrenome com o caractere “#”.
"""
nome_completo = (input("Por favor digite seu nome completo: ").split(" "))

ultimo_sobrenome = nome_completo[-1]

print (len(ultimo_sobrenome) * "#")
