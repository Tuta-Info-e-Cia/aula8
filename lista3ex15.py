"""
15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

n = int(input("Digite quantos termos da série de Fibonacci você quer gerar: "))

fib1, fib2 = 1, 1

if n <= 0:
    print("Digite um número positivo.")
elif n == 1:
    print("Série de Fibonacci até o 1º termo:")
    print(fib1)
else:
    print(f"Série de Fibonacci até o {n}º termo:")
    print(fib1, fib2, end=' ')
    for _ in range(3, n+1):
        fib = fib1 + fib2
        print(fib, end=' ')
        fib1, fib2 = fib2, fib
    print()

    