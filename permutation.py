
#!/bin/env python3

# TP sur les permutations

# Saisie des variables
# Je ne cast pas les variables, l'inversion proposée fonctionne quelque soit le type de données
x = input("Saisir x : ")
y = input("Saisir y : ")

print("Avant permutation : ")
print("\tx :", x)
print("\ty :", y)

# Permutation
c = x
x = y
y = c

print("Après permutation : ")
print("\tx :", x)
print("\ty :", y)

# Permutation par combinaison linéaire
# Ceci est une permutation linéaire avec des nombres (ici des réels)
x = float(input("Saisir x : "))
y = float(input("Saisir y : "))

print("Avant permutation : ")
print("\tx :", x)
print("\ty :", y)

# Permutation
x = x + y
y = x - y
x = x - y

print("Après permutation : ")
print("\tx :", x)
print("\ty :", y)
