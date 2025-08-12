"""
11. Altere o programa anterior para mostrar no final a soma dos números.
"""

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

inicio = min(num1, num2) + 1
fim = max(num1, num2)

soma = 0

print(f"Números entre {num1} e {num2}:")
for num in range(inicio, fim):
    print(num)
    soma += num

print(f"Soma dos números no intervalo: {soma}")


