#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math
from pathlib import Path

Path("images").mkdir(exist_ok=True)

def ouvrirUnFichier(nom):
    try:
        return pd.read_csv(nom, encoding="utf-8", low_memory=False)
    except UnicodeDecodeError:
        return pd.read_csv(nom, encoding="latin-1", low_memory=False)


def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element][1]])
    return classement

iles = pd.DataFrame(ouvrirUnFichier("src/data/island-index.csv"))
iles.columns = iles.columns.str.strip()

surfaces = list(iles["Surface (km²)"])

surfaces.append(85545323)
surfaces.append(37856841)
surfaces.append(7768030)
surfaces.append(7605049)

# Nettoyage
surfaces = [float(s) for s in surfaces if s > 0]
surfaces = ordreDecroissant(surfaces)
rangs = list(range(1, len(surfaces) + 1))

plt.figure()
plt.plot(rangs, surfaces)
plt.title("Loi rang-taille des îles")
plt.xlabel("Rang")
plt.ylabel("Surface (km²)")
plt.tight_layout()
plt.savefig("images/graph1.png")
plt.close()

log_rangs = conversionLog(rangs)
log_surfaces = conversionLog(surfaces)

plt.figure()
plt.plot(log_rangs, log_surfaces)
plt.title("Loi rang-taille des îles (log-log)")
plt.xlabel("log(rang)")
plt.ylabel("log(surface)")
plt.tight_layout()
plt.savefig("images/log.png")
plt.close()


# Il n'est pas possible d'appliquer un test statistique classique sur les rangs seuls,
# car les rangs sont des variables ordinales et non quantitatives indépendantes.




monde = pd.DataFrame(ouvrirUnFichier("src/data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))

etats = list(monde["État"])
pop2007 = list(monde["Pop 2007"])
dens2007 = list(monde["Densité 2007"])

classement_pop2007 = ordrePopulation(pop2007, etats)
classement_dens2007 = ordrePopulation(dens2007, etats)

comparaison = classementPays(classement_pop2007, classement_dens2007)
comparaison.sort()

rangs_pop = []
rangs_dens = []

for element in comparaison:
    rangs_pop.append(element[0])
    rangs_dens.append(element[1])

spearman = scipy.stats.spearmanr(rangs_pop, rangs_dens)
kendall = scipy.stats.kendalltau(rangs_pop, rangs_dens)

print("Spearman :", spearman)
print("Kendall :", kendall)





