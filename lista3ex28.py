"""
28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.

"""

while True:
    try:
        qtd_cds = int(input("Digite a quantidade de CDs na coleção: "))
        if qtd_cds > 0:
            break
        else:
            print("A quantidade de CDs deve ser maior que zero.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

total_investido = 0.0


for i in range(1, qtd_cds + 1):
    while True:
        try:
            valor = float(input(f"Digite o valor pago pelo CD {i}: R$ "))
            if valor >= 0:
                total_investido += valor
                break
            else:
                print("O valor não pode ser negativo.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")


media = total_investido / qtd_cds

print(f"\nValor total investido: R$ {total_investido:.2f}")
print(f"Valor médio por CD: R$ {media:.2f}")

