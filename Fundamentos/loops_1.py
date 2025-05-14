# exemplo simples de loop com lista ↓

frutas = ["banana", "maçã", "uva", "morango", "pinguim russo de guerra"] 
for f in frutas:
    print(f)

print("\n")
# iterar pelos caracteres ↓

nome = "Luva de Pedreiro"
for letra in nome:
    print(letra)

print("\n")
# exemplo de loop coom "enumerate" e condição ↓

notas = [7.5, 8.0, 6.0, 9.2]

for i, nota in enumerate(notas):
    if nota >=7:
        print(f"Aluno n° {i+1} aprovado com a nota {nota}")
    else:
        print(f"Aluno n° {i+1} reprovado com a nota {nota}")

print("\n\n")
# exeplo de loop aninhado com dicionário de listas:

teams = {
    "Lakers": ["Anthony Davis", "LeBron James", "Luka Dončić", "Austin Reaves", "Rui Hachimura"],
    "Dream Team": ["Michael Jordan", "Magic Johnson", "Larry Bird", "Charles Barkley", "David Robinson"]
}

for team, players in teams.items():
    print(f"\n{team} players:")
    for player in players:
        print(f" - {player}")
