'''ler numero de vendedor, salario fixo e total de vendas efetuadas por ele no mes (em dinheiro).
comissão = 15% sobre as vendas

informar (output) o total a receber no final do mes em float com .2f

input:
nome do vendedor
2 valores float com formatação .2f representando o salario fixo e o montate total das vendas efetuadas

output valor total que func recebera'''

vendedor = input("")
salario_fixo = float(input(""))
total_vendas_mes = float(input(""))
comissao = total_vendas_mes * 0.15

valor_total = comissao + salario_fixo

print(f"TOTAL = R$ {valor_total:.2f}")
