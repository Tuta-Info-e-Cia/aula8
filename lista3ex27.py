"""
27. Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.
"""

while True:
    try:
        num_turmas = int(input("Digite a quantidade de turmas: "))
        if num_turmas > 0:
            break
        else:
            print("A quantidade de turmas deve ser maior que zero.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

total_alunos = 0

for i in range(1, num_turmas + 1):
    while True:
        try:
            alunos = int(input(f"Digite a quantidade de alunos da turma {i} (máximo 40): "))
            if 0 < alunos <= 40:
                total_alunos += alunos
                break
            else:
                print("Cada turma deve ter entre 1 e 40 alunos.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

media = total_alunos / num_turmas
print(f"\nMédia de alunos por turma: {media:.2f}")

