"""
21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.

"""

num = int(input("Digite um número inteiro: "))
if num <= 1:
    print(f"{num} não é primo.")
else:
    eh_primo = True
    for i in range(2, int(num**0.5) + 1):  # Testa até a raiz quadrada de num
        if num % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")

        