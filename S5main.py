#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats




def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu


print("Résultat sur le calcul d'un intervalle de fluctuation")

donnees = pd.DataFrame(ouvrirUnFichier("src/data/Echantillonnage-100-Echantillons.csv"))


population = {
    "Pour": 852,
    "Contre": 911,
    "Sans opinion": 422
}

moyennes = donnees.mean()
moyennes = moyennes.round(0)

print("Moyennes des échantillons :")
print(moyennes)

total_moyennes = moyennes.sum()
frequences_obs = moyennes / total_moyennes
frequences_obs = frequences_obs.round(2)

print("\nFréquences observées :")
print(frequences_obs)

total_pop = sum(population.values())
frequences_pop = {
    k: round(v / total_pop, 2) for k, v in population.items()
}

print("\nFréquences population mère :")
print(frequences_pop)

z = 1.96

print("\nIntervalles de fluctuation (95 %) :")
for col in donnees.columns: 
    p = frequences_obs[col]
    n = total_moyennes
    marge = z * math.sqrt((p * (1 - p)) / n)
    print(col, ":", round(p - marge, 3), "-", round(p + marge, 3))
      


print("Résultat sur le calcul d'un intervalle de confiance")



echantillon = list(donnees.iloc[0])
total = sum(echantillon)

frequences = [x / total for x in echantillon]

print("Fréquences de l'échantillon :")
print([round(f, 2) for f in frequences])

print("\nIntervalles de confiance (95 %) :")
for f in frequences: 
    marge = z * math.sqrt((f * (1 - f)) / total)
    print(round(f - marge, 3), "-", round (f + marge, 3))


print("Théorie de la décision")

import numpy as np

data1 = pd.read_csv("src/data/Loi-normale-Test-1.csv").values.flatten()
data2 = pd.read_csv("src/data/Loi-normale-Test-2.csv").values.flatten()

stat1, p1 = scipy.stats.shapiro(data1)
stat2, p2 = scipy.stats.shapiro(data2)

print("Test 1 : p-value =", p1)
print("Test 2 : p-value =", p2)

if p1 > 0.05:
    print("Le test 1 suit une loi normale")
else:
    print("Le test 1 ne suit pas une loi normale")

if p2 > 0.05:
    print("Le test 2 suit une loi normale")
else:
    print("Le test 2 ne suit pas une loi normale")

print(len(data1), len(data2))

