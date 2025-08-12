"""
17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

num = int(input("Digite um número inteiro para calcular o fatorial: "))

if num < 0:
    print("Fatorial não é definido para números negativos.")
elif num == 0 or num == 1:
    print(f"{num}! = 1")
else:
    fatorial = 1
    print(f"{num}! = ", end='')
    for i in range(num, 0, -1):
        print(i, end='.' if i > 1 else ' = ')
        fatorial *= i
    print(fatorial)


    