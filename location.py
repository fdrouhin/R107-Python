#!/usr/bin/env python3

# Prix d'une location
heurePleineDebut = 7
heurePleineFin = 18

# Saisie des heures de début et de fin
debut = int(input("Saisir une heure de début : "))
fin = int(input("Saisir une heure de fin : "))

if debut < 0 or debut > 23 or fin < 0 or fin > 23 or debut >= fin:
    print("Les heures de début et de fin doivent être dans 0, 23")
    exit(2)

hp = 0
hc = 0
for x in range(debut, fin+1):
    if x in range(heurePleineDebut, heurePleineFin+1):
        hp = hp + 1
    else:
        hc = hc + 1


print("Nombre d'heures pleines : ", hp)
print("Nombre d'heures creuses : ", hc)
prix = hp * 2 + hc * 1
print("Le prix de localion est de", prix, "euros")

