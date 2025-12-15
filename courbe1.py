import matplotlib.pyplot as plt

temps = []
vitesse = []
temperature = []

with open("Donnees.csv", "r", encoding="utf-8-sig") as fichier:
    next(fichier)  # Ignore la première ligne du fichier
    
    for ligne in fichier:
        ligne = ligne.strip()
        donnees = ligne.split(";")

        if len(donnees) > 6: #Vérifie que la liste contient au moins 7 éléments.
            #TEMPS
            hms = donnees[0]   #Récupère la colonne 0 du fichier          
            h, m, s = hms.split(":")  #coupe la chaine de caractere en  3 partie (separateur":")
            t = int(h)*3600 + int(m)*60 + float(s)#Convertit le temps en secondes

            #VITESSE
            v = float(donnees[5].replace(",", "."))#Récupère la valeur de la colonne 5,et remplace la virgule par un point

            #TEMPERATURE
            temp = float(donnees[6].replace(",", "."))#Récupère la valeur de la colonne 6,et remplace la virgule par un point

            temps.append(t)
            vitesse.append(v)
            temperature.append(temp)

#  TRACÉ LES DEUX COURBES 
plt.plot(temps, vitesse, label="Vitesse")
plt.plot(temps, temperature, label="Température")

plt.xlabel("Temps (s)")
plt.ylabel("Valeur")
plt.title("Vitesse et température du ballon sonde en fonction du temps")
plt.grid(True)
plt.legend()
plt.show()




