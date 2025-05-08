'''calcular consumo medio de carro sendo fornecio:
distancia total percorrida (em km)
total de combustivel gasto (em L)

entrada:
inteiro = distancia_total
float = combustivel_gasto

saida:
apresentar valor medio com formatação .3f, seguido de "km/l"'''

distancia_total = int(input(""))
combustivel_gasto = float(input(""))

km_l = distancia_total / combustivel_gasto

print(f"{km_l:.3f} km/l")