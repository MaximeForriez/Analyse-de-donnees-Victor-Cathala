#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023

with open("src/data/resultats-elections-presidentielles-2022-1er-tour.csv","r",encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier, sep=",")

Path("images").mkdir(exist_ok=True)

print(contenu.head())

print (contenu.shape)

print (contenu.dtypes)

print (contenu.columns)

print (contenu.head())

print (contenu["Inscrits"].head())

colonnes_numériques = contenu.select_dtypes(include=["int64","float64"])
print (colonnes_numériques.sum())
Path("images").mkdir(exist_ok=True)

for i, row in contenu.iterrows():
    dept= str(row["Libellé du département"]).replace(" ","_").replace("/","-")

    plt.figure()
    plt.bar(["Inscrits","Votants"],[row["Inscrits"],row["Votants"]])
    plt.title(dept)
    plt.tight_layout()
    plt.savefig(f"images/bar_{i}_{dept}.png")
    plt.close()


for i, row in contenu.iterrows(): 
    dept = str(row["Libellé du département"]).replace(" ","_").replace("/","-")

    valeurs= [
        row["Blancs"],
        row["Nuls"],
        row["Exprimés"],
        row["Abstentions"]
    ]
    labels= ["Blancs","Nuls","Exprimés","Abstentions"]

    plt.figure()
    plt.pie(valeurs, labels=labels, autopct="%1.1f%%")
    plt.title(dept)
    plt.tight_layout()
    plt.savefig(f"images/pie_{i}_{dept}.png")
    plt.close()

plt.figure()
plt.hist(contenu["Inscrits"], bins=30, density=True)
plt.title("Distribution des inscrits")
plt.xlabel("Inscrits")
plt.ylabel("Densité")
plt.tight_layout()
plt.savefig("images/hist_inscrits.png")
plt.close()

colonnes_quantitatives = contenu.select_dtypes(include=["int64", "float64"])

noms = list(colonnes_quantitatives.columns)

moyennes = list(colonnes_quantitatives.mean().round(2))

médianes = list(colonnes_quantitatives.median().round(2))

modes = []
for col in noms :
    serie = colonnes_quantitatives[col].dropna()
    mode_col = serie.mode()
    modes.append(round(float(mode_col.iloc[0]),2) if len(mode_col) > 0 else None)

ecarts_types = list(colonnes_quantitatives.std().round(2))

ecarts_absolus_moy = []
for col in noms :
    serie = colonnes_quantitatives[col].dropna()
    m = serie.mean()
    ecarts_absolus_moy.append(round(float(np.abs(serie - m).mean()), 2))

etendues = []
for col in noms : 
    serie = colonnes_quantitatives[col].dropna()
    etendues.append(round(float(serie.max() - serie.min()), 2))

print("\n--- Colonnes quantitatives ---")
print(noms)

print("\n--- Paramètres (dans le même ordre que noms) ---")
print("Moyennes :", moyennes)
print("Médianes :", médianes)
print("Modes :", modes)
print("Ecarts-types :", ecarts_types)
print("Ecarts absolus à la moyenne :", ecarts_absolus_moy)
print ("Etendues :", etendues)

iqr = list((colonnes_quantitatives.quantile(0.75) - colonnes_quantitatives.quantile(0.25)).round(2))
idr = list((colonnes_quantitatives.quantile(0.90) - colonnes_quantitatives.quantile(0.10)).round(2))

print("\n--- Distances ---")
print("Interquartile (Q3-Q1) :", iqr)
print("Interdécile (D9-D1) :", idr)

for col in noms: 
    plt.figure()
    plt.boxplot(colonnes_quantitatives[col].dropna(), vert=True)
    plt.title(f"Boxplot - {col}")
    plt.tight_layout()
    plt.savefig(f"images/boxplot_{col}.png")
    plt.close()

with open("src/data/island-index.csv", "r", encoding="utf-8") as fichier2:
    islands = pd.read_csv(fichier2)

print("\n--- Colonnes island-index ---")
print(islands.columns)

surface = islands ["Surface (km²)"]

c_0_10 = 0
c_10_25 = 0
c_25_50 = 0
c_50_100 = 0
c_100_2500 = 0
c_2500_5000 = 0
c_5000_10000 = 0
c_10000_plus = 0

for s in surface.dropna():
    if 0 < s <=10:
        c_0_10 += 1
    elif 10 < s <= 25:
        c_10_25 += 1
    elif 25 < s <= 50:
        c_25_50 += 1
    elif 50 < s <= 100:
        c_50_100 += 1
    elif 100 < s <= 2500:
        c_100_2500 +=1
    elif 2500 < s <= 5000:
        c_2500_5000 += 1
    elif 5000 < s <= 10000:
        c_5000_10000 +=1
    elif s >= 10000:
        c_10000_plus += 1

print("\n--- Catégories Surface (km²) ---")
print("]0, 10]      :", c_0_10)
print("]10, 25]     :", c_10_25)
print("]25, 50]     :", c_25_50)
print("]50, 100]    :", c_50_100)
print("]100, 2500]  :", c_100_2500)
print("]2500, 5000] :", c_2500_5000)
print("]5000, 10000]:", c_5000_10000)
print("]10000, +∞[  :", c_10000_plus)

