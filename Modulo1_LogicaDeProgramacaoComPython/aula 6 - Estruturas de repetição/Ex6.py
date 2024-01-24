"""
Escreva um programa que exiba os números de 1 a 100, substituindo os
múltiplos de 3 pela palavra "Fizz", os múltiplos de 5 pela palavra "Buzz" e
os múltiplos de ambos (3 e 5) pela palavra "FizzBuzz"
"""

for i in range (0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    print(i)

