"""
14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

pares = 0
impares = 0

for i in range(10):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
