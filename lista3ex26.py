"""
26. Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

"""

while True:
    try:
        total_eleitores = int(input("Digite o número total de eleitores: "))
        if total_eleitores > 0:
            break
        else:
            print("Digite um número maior que zero.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

votos_cand1 = 0
votos_cand2 = 0
votos_cand3 = 0

print("\nCandidatos:")
print("1 - Candidato 1")
print("2 - Candidato 2")
print("3 - Candidato 3\n")

for i in range(1, total_eleitores + 1):
    while True:
        try:
            voto = int(input(f"Eleitor {i}, digite seu voto (1, 2 ou 3): "))
            if voto == 1:
                votos_cand1 += 1
                break
            elif voto == 2:
                votos_cand2 += 1
                break
            elif voto == 3:
                votos_cand3 += 1
                break
            else:
                print("Voto inválido! Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


print("\nResultado da eleição:")
print(f"Candidato 1: {votos_cand1} voto(s)")
print(f"Candidato 2: {votos_cand2} voto(s)")
print(f"Candidato 3: {votos_cand3} voto(s)")


