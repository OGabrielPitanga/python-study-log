# Lê a primeira linha e separa os valores
codigo1, quantidade1, valor1 = input().split()
codigo1 = int(codigo1)
quantidade1 = int(quantidade1)
valor1 = float(valor1)

# Lê a segunda linha e separa os valores
codigo2, quantidade2, valor2 = input().split()
codigo2 = int(codigo2)
quantidade2 = int(quantidade2)
valor2 = float(valor2)

# Calcula o valor total a ser pago
total = (quantidade1 * valor1) + (quantidade2 * valor2)

# Imprime o resultado com formatação correta
print(f"VALOR A PAGAR: R$ {total:.2f}")

##COPIADO DO CHAT GPT pois nao sabia como usar o split e aprendi hoje