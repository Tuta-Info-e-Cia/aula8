"""
25. Faça um programa que peça para n pessoas a sua idade, 
ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

while True:
    try:
        n = int(input("Quantas pessoas tem na turma? "))
        if n > 0:
            break
        else:
            print("Digite um número maior que zero.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")


soma_idades = 0
for i in range(1, n + 1):
    while True:
        try:
            idade = int(input(f"Digite a idade da pessoa {i}: "))
            if idade >= 0:
                soma_idades += idade
                break
            else:
                print("Idade não pode ser negativa.")
        except ValueError:
            print("Entrada inválida! Digite uma idade válida.")

media = soma_idades / n

print(f"\nMédia de idade da turma: {media:.2f}")

if media <= 25:
    print("A turma é considerada JOVEM.")
elif 26 <= media <= 60:
    print("A turma é considerada ADULTA.")
else:
    print("A turma é considerada IDOSA.")


