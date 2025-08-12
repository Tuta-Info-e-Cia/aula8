"""
22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

"""

num = int(input("Digite um número inteiro: "))

if num <= 1:
    print(f"{num} não é primo.")
else:
    divisores = []

    for i in range(2, num):
        if num % i == 0:
            divisores.append(i)

    if not divisores:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é primo.")
        print(f"Ele é divisível por: {divisores}")

        