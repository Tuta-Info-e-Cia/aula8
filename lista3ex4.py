"""
4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

"""

pop_A = 80000
pop_B = 200000

taxa_A = 0.03
taxa_B = 0.015

anos = 0

while pop_A < pop_B:
    pop_A += pop_A * taxa_A
    pop_B += pop_B * taxa_B
    anos += 1

print(f"Serão necessários {anos} anos para a população do país A ultrapassar ou igualar a do país B.")
print(f"População do país A: {int(pop_A)}")
print(f"População do país B: {int(pop_B)}")

