'''
autonomia do carro = 12 km/l
deve-se fornceer tempo gasto na viagem em horas e velocidade media da viagem
assim, obbter a distancia percorrida e calcular litros necessarios
mosrar com formatacao .3f

entrada: 
    int = tempo gasto em horas
    int = velocidade media durante viagem em km/h

saida:
    quantidade de litros necessaria com format .3f
'''

tempo_gasto = int(input(""))
velocidade_media = int(input(""))

total_litros = (tempo_gasto * velocidade_media) / 12

print(f"{total_litros:.3f}")