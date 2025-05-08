'''ler numero de funcionario + numero de horas trabalhadas + valor que recebe por hora
calcular salario do funcionario baseado nos dados de entrada
mostrar o numero do funcionario + o salario (formatar com .2f)

inputs:
2 int e 1 float com 2 casas (.2f)

output:
numero do funcionario 
salario
'''
num_func = int(input(""))
horas_trabalhadas = int(input(""))
valor_hora = float(input(""))

salario = horas_trabalhadas * valor_hora

print(f"NUMBER = {num_func}")
print(f"SALARY = U${salario: .2f}")
