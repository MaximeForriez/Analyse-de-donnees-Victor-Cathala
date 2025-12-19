#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("src/data/resultats-elections-presidentielles-2022-1er-tour.csv","r",encoding="utf-8") as fichier:
    contenu= pd.read_csv(fichier, sep=",")
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
