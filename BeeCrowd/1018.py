x = int(input(""))
print(x)

cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    qtd = x // cedula
    print(f"{qtd} nota(s) de R$ {cedula},00")
    x = x % cedula