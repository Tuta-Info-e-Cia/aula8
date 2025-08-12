"""
24. Faça um programa que calcule o mostre a média aritmética de N notas.

"""

while True:
    try:
        N = int(input("Quantas notas você vai informar? "))
        if N > 0:
            break
        else:
            print("Digite um número maior que zero.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

soma = 0
for i in range(1, N+1):
    while True:
        try:
            nota = float(input(f"Digite a nota {i}: "))
            soma += nota
            break
        except ValueError:
            print("Entrada inválida! Digite uma nota válida.")

media = soma / N

print(f"\nA média aritmética das {N} notas é: {media:.2f}")

