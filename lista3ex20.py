"""
20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""

while True:

    while True:
        try:
            num = int(input("Digite um número inteiro entre 0 e 15 para calcular o fatorial: "))
            if 0 <= num < 16:
                break
            else:
                print("Número fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    fatorial = 1
    print(f"{num}! = ", end='')

    if num == 0 or num == 1:
        print("1 = 1")
    else:
        for i in range(num, 0, -1):
            fatorial *= i
            print(i, end='.' if i > 1 else ' = ')
        print(fatorial)


    continuar = input("\nDeseja calcular outro fatorial? (s/n): ").strip().lower()
    if continuar != 's':
        print("Programa encerrado.")
        break
