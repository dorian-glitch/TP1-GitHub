import matplotlib.pyplot as plt

# --- COMMUNES DE L'AGGLOMERATION IMMEDIATE ---
agglomeration_immediate = [
    "Appoigny", "Auxerre", "Monéteau", "Perrigny", "Saint-Georges-sur-Baulche"
]

# --- FONCTION POUR EXTRAIRE LA POPULATION ---
def population_communes(fichier, communes):
    total = 0
    trouve = False
    with open(fichier, "r", encoding="utf8") as fic:
        next(fic)  # sauter l'en-tête
        for ligne in fic:
            ligne = ligne.strip().strip('"').strip("'")  # enlever guillemets et espaces
            cols = ligne.split(',')
            if len(cols) < 10:
                continue
            nom_commune = cols[6].strip().lower()
            if nom_commune in [c.lower() for c in communes]:
                try:
                    pop = int(cols[9].replace(' ', ''))
                    total += pop
                    trouve = True
                except ValueError:
                    print(f"Erreur conversion population pour {cols[6]} dans {fichier}")
    if not trouve:
        print(f"Aucune commune trouvée dans {fichier} parmi {communes}")
        return None
    return total

# --- FICHIERS ET ANNEES ---
fichiers = ["donnees_2008.csv", "donnees_2016.csv", "donnees_2021.csv", "donnees_2023.csv"]
annees = [2008, 2016, 2021, 2023]

# --- EXTRACTION DES POPULATIONS ---
pop_auxerre = [population_communes(f, ["Auxerre"]) for f in fichiers]
pop_agglomeration = [population_communes(f, agglomeration_immediate) for f in fichiers]

print("Population Auxerre :", pop_auxerre)
print("Population agglomération immédiate :", pop_agglomeration)

# --- TRACÉ DU GRAPHIQUE ---
plt.plot(annees, pop_auxerre, marker='o', linestyle='-', color='blue', label="Auxerre")
plt.plot(annees, pop_agglomeration, marker='s', linestyle='--', color='red', label="Agglomération immédiate")
plt.xlabel("Année")
plt.ylabel("Population")
plt.title("Évolution de la population d'Auxerre et de son agglomération")
plt.grid(True)
plt.legend()
plt.show()
