N = int(input("Entrez un nombre entier : "))

factorielle = 1

for i in range(1, N + 1):
    factorielle *= i

print(f"La factorielle de {N} est : {factorielle}")