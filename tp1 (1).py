import matplotlib.pyplot as plt

# --- COMMUNES ---
agglomeration_immediate = ["Appoigny", "Auxerre", "Monéteau", "Perrigny", "Saint-Georges-sur-Baulche"]

agglomeration_totale = [
    "Appoigny", "Augy", "Auxerre", "Bleigny-le-Carreau", "Branches", "Champs-sur-Yonne",
    "Charbuy", "Chevannes", "Chitry", "Coulanges-la-Vineuse", "Escamps", "Escolives Sainte-Camille",
    "Gurgy", "Gy-l’Evêque", "Irancy", "Jussy", "Lindry", "Monéteau", "Montigny-la-Resle", "Perrigny",
    "Quenne", "Saint-Bris-le-Vineux", "Saint-Georges-sur-Baulche", "Vallan", "Venoy", "Villefargeau",
    "Villeneuve-Saint-Salves", "Vincelles", "Vincelottes"
]

# --- FONCTION POUR EXTRAIRE LA POPULATION ---
def population_communes(fichier, communes=None, code_departement=None):
    total = 0
    trouve = False
    with open(fichier, "r", encoding="utf8") as fic:
        next(fic)  # sauter l'en-tête
        for ligne in fic:
            ligne = ligne.strip().strip('"').strip("'")
            cols = ligne.split(',')
            if len(cols) < 10:
                continue
            nom_commune = cols[6].strip().lower()
            dep_code = cols[2].strip()
            
            if communes:
                if nom_commune in [c.lower() for c in communes]:
                    try:
                        pop = int(cols[9].replace(' ', ''))
                        total += pop
                        trouve = True
                    except ValueError:
                        print(f"Erreur conversion population pour {cols[6]}")
            elif code_departement:
                if dep_code == code_departement:
                    try:
                        pop = int(cols[9].replace(' ', ''))
                        total += pop
                        trouve = True
                    except ValueError:
                        print(f"Erreur conversion population pour {cols[6]}")
                    
    if not trouve:
        print(f"Aucune donnée trouvée dans {fichier} pour {communes if communes else 'département ' + code_departement}")
        return None
    return total

# --- FICHIERS ET ANNEES ---
fichiers = ["donnees_2008.csv", "donnees_2016.csv", "donnees_2021.csv", "donnees_2023.csv"]
annees = [2008, 2016, 2021, 2023]

# --- EXTRACTION DES POPULATIONS ---
pop_auxerre = [population_communes(f, ["Auxerre"]) for f in fichiers]
pop_agglomeration = [population_communes(f, agglomeration_immediate) for f in fichiers]
pop_agglomeration_totale = [population_communes(f, agglomeration_totale) for f in fichiers]
pop_departement = [population_communes(f, code_departement="89") for f in fichiers]

# --- AFFICHAGE ---
print("Population Auxerre :", pop_auxerre)
print("Population agglomération immédiate :", pop_agglomeration)
print("Population agglomération totale :", pop_agglomeration_totale)
print("Population département Yonne :", pop_departement)

# --- TRACÉ DU GRAPHIQUE ---
plt.plot(annees, pop_auxerre, marker='o', linestyle='-', color='blue', label="Auxerre")
plt.plot(annees, pop_agglomeration, marker='s', linestyle='--', color='red', label="Agglo immédiate")
plt.plot(annees, pop_agglomeration_totale, marker='^', linestyle='-.', color='green', label="Agglo totale")
plt.plot(annees, pop_departement, marker='x', linestyle=':', color='orange', label="Département")
plt.xlabel("Année")
plt.ylabel("Population")
plt.title("Évolution de la population d'Auxerre et de l'Yonne")
plt.grid(True)
plt.legend()
plt.show()
