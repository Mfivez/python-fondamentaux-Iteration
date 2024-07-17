N = int(input("Entrez le nombre de termes de la suite de Fibonacci à afficher : "))

a, b = 0, 1

for _ in range(N):
    print(a)
    a, b = b, a + b