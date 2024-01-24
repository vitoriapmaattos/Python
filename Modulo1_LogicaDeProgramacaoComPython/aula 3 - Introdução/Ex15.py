"""
Faça um programa que receba o
tamanho de um arquivo em GB e mostre o valor em
"""
tamanho = int(input("Digite o tamanho do arquivo em GB: "))

mb = tamanho * 1024
kb = mb * 1024
byte = kb * 1024
bits = byte * 8

print(f"O tamanho em MB é: {mb}")
print(f"O tamanho em KB é: {kb}")
print(f"O tamanho em Bytes é: {byte}")
print(f"O tamanho em bits é: {bits}")