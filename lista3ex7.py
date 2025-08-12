"""
7. Faça um programa que leia 5 números e informe o maior e o menor número.
"""

maior = float ('-inf')
menor = float ('inf')
for i in range(5):
    n = int(input(f'Digite o {i+1}º número: '))
    if maior < n :
        maior = n
    if menor > n:
        menor = n    
print(f'O maior número entre os digitados é: {maior}')
print(f'O menor número entre os digitados é: {menor}')
