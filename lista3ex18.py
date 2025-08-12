"""
18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

while True:
    try:
        N = int(input("Quantos números você vai digitar? "))
        if N > 0:
            break
        else:
            print("Digite um número maior que zero.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
numeros = []
for i in range(N):
    while True:
        try:
            num = float(input(f"Digite o {i+1}º número: "))
            numeros.append(num)
            break
        except ValueError:
            print("Entrada inválida! Digite um número.")

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")

