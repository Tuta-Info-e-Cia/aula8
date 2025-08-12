"""
3. Faça um programa que leia e valide as seguintes informações:
- Nome: maior que 3 caracteres;
- Idade: entre 0 e 150;
- Salário: maior que zero;
- Sexo: 'f' ou 'm';
- Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = input("Digite o nome (mais de 3 caracteres): ").strip()
    if len(nome) > 3:
        break
    else:
        print("Nome inválido! Deve ter mais de 3 caracteres.")

while True:
    try:
        idade = int(input("Digite a idade (0 a 150): "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade inválida! Deve estar entre 0 e 150.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

while True:
    try:
        salario = float(input("Digite o salário (maior que zero): "))
        if salario > 0:
            break
        else:
            print("Salário inválido! Deve ser maior que zero.")
    except ValueError:
        print("Entrada inválida! Digite um número.")

while True:
    sexo = input("Digite o sexo ('f' ou 'm'): ").lower()
    if sexo in ['f', 'm']:
        break
    else:
        print("Sexo inválido! Digite 'f' ou 'm'.")

while True:
    estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil inválido! Digite 's', 'c', 'v' ou 'd'.")


print("\nDados cadastrados com sucesso:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

