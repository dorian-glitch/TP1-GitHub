import matplotlib.pyplot as plt

altitude = []
temp_ext = []
temp_int = []

with open("Donnees.csv", "r", encoding="utf-8-sig") as fichier:
    next(fichier)  # sauter l'en-tête

    for ligne in fichier:
        ligne = ligne.strip()
        donnees = ligne.split(";")

        if len(donnees) > 7:
            # ----- ALTITUDE -----
            alt = float(donnees[4].replace(",", "."))

            # ----- TEMPERATURE EXTERIEURE -----
            t_ext = float(donnees[6].replace(",", "."))

            # ----- TEMPERATURE INTERIEURE -----
            t_int = float(donnees[7].replace(",", "."))

            altitude.append(alt)
            temp_ext.append(t_ext)
            temp_int.append(t_int)

# ----- TRACE DU GRAPHIQUE -----
plt.plot(altitude, temp_ext, label="Température extérieure")
plt.plot(altitude, temp_int, label="Température intérieure")

plt.xlabel("Altitude (m)")
plt.ylabel("Température (°C)")
plt.title("Température intérieure et extérieure en fonction de l'altitude")
plt.grid(True)
plt.legend()
plt.show()
