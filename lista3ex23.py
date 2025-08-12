"""
23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

N = int(input("Digite um número inteiro maior que 1: "))

if N <= 1:
    print("Digite um número maior que 1.")
else:
    total_divisoes = 0
    primos = []

    for num in range(2, N+1):
        eh_primo = True
        for i in range(2, int(num**0.5) + 1):
            total_divisoes += 1
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(num)

    print(f"Números primos entre 1 e {N}:")
    print(primos)
    print(f"\nNúmero total de divisões realizadas: {total_divisoes}")
    

    