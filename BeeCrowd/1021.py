valor = float(input())
centavos = int(round(valor * 100))

notas_centavos = [10000, 5000, 2000, 1000, 500, 200]
moedas_centavos = [100, 50, 25, 10, 5, 1]

print("NOTAS: ")
for nota in notas_centavos:
    quantidade = centavos // nota
    print(f"{quantidade} nota(s) de R${nota / 100:.2f}")
    centavos %= nota

print("MOEDAS:")
for moeda in moedas_centavos:
    quantidade = centavos // moeda
    print(f"{quantidade} moeda(s) de R$ {moeda / 100:.2f}")
    centavos %= moeda