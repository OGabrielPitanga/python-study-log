a, b, c = map(int, input().split())

maior = a 

if b > maior:
        maior = b

if c > maior:
        maior = c

print(f"{maior} eh o maior")