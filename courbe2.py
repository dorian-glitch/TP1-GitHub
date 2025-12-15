import csv
from datetime import datetime
import matplotlib.pyplot as plt

donnee_brute = []

with open('Donnees.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        donnee_brute.append(row)

en_tete = donnee_brute[0]
donnees_vol = donnee_brute[1:]

IDX_DATETIME = 0
IDX_ALTITUDE = 3
IDX_TEMP_INT = 5
IDX_TEMP_EXT = 6

temps_s = []
altitudes = []
temp_ext = []

try:
    temps_depart_str = donnees_vol[0][IDX_DATETIME]
    temps_depart = datetime.strptime(temps_depart_str, '%H:%M:%S.%f')
except ValueError:
    temps_depart = datetime.strptime(
        temps_depart_str.split('.')[0],
        '%H:%M:%S'
    )

for ligne in donnees_vol:
    try:
        temps_actuel_str = ligne[IDX_DATETIME]

        try:
            temps_actuel = datetime.strptime(
                temps_actuel_str,
                '%H:%M:%S.%f'
            )
        except ValueError:
            temps_actuel = datetime.strptime(
                temps_actuel_str.split('.')[0],
                '%H:%M:%S'
            )

        temps_ecoule = (temps_actuel - temps_depart).total_seconds()
        temps_s.append(temps_ecoule)
        altitudes.append(float(ligne[IDX_ALTITUDE]))
        temp_ext.append(float(ligne[IDX_TEMP_EXT]))

    except (ValueError, IndexError):
        continue

temps_minutes = [t / 60 for t in temps_s]  # Passer en minutes pour le graphique

plt.figure(figsize=(12, 6))
plt.plot(temps_minutes, altitudes, label='Altitude', color='blue')
plt.title('Profil de vol du ballon sonde (Altitude vs. Temps)')
plt.xlabel('Temps écoulé (minutes)')
plt.ylabel('Altitude (mètres)')
plt.grid(True)
plt.legend()
plt.show()

# Visualisation de la Température Extérieure vs. Altitude

plt.figure(figsize=(10, 7))
plt.scatter(temp_ext, altitudes, s=5, alpha=0.6, color='red')
plt.title("Température Extérieure en fonction de l'Altitude")
plt.xlabel('Température Extérieure (°C)')
plt.ylabel('Altitude (mètres)')
plt.grid(True)
plt.show()
