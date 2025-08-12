"""
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

"""

while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break
        else:
            print("Valor inválido! A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número.")

        