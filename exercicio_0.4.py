soma = 0

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

media = soma / 5

print(f"A média aritmética dos números informados é: {media:.2f}")
