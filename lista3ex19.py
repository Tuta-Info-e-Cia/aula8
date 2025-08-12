"""
19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

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
            num = float(input(f"Digite o {i+1}º número (entre 0 e 1000): "))
            if 0 <= num <= 1000:
                numeros.append(num)
                break
            else:
                print("Número fora do intervalo permitido (0 a 1000).")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")



