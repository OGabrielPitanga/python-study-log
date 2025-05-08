'''ler 4 valores: eixo x e y DE 2 PONTOS
p1(x1, y1) e p2(x2, y2)

calcular a distancia entre eles, mostrando 4 casas decimais

formula = raiz de (x2 - x2) **2 + (y2 - y1) ** 2

ENTRADA:
duas linhas
	1 - 2 float = x1, y1
	2 - 2 float = x2, y2

SAIDA:
calcular e imprimir valor da distancia com format .4f'''

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"{distancia:.4f}")
