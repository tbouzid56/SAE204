import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importer le csv dans le python
df_formation =  pd.read_csv("export_csv.csv", sep=";") #ici, préciser le séparateur du csv permet d'évite que les cases contiennes tous des guillemets 
# test pour voir si c'est bien dans la variable
#print(df_formation.head())
#print(df_formation.columns)



# Passer ensuite en numpy.array les données de df_num_lannion :
arr_formation = df_formation.to_numpy() 
# print(arr_formation)


taux_acces = arr_formation[:,0]
#print(taux_acces)


rang_dernier_appele_groupe1 = arr_formation[:,1]
#print(rang_dernier_appele_groupe1)


effectif_total_candidats = arr_formation[:,2]
#print(effectif_total_candidats)

departement_code = arr_formation[:,3]
#print(departement_code)



# Boites a moustaches 
liste_boites = [taux_acces, departement_code]
plt.boxplot(liste_boites)
plt.show()


# Nuage de points

plt.plot(effectif_total_candidats, taux_acces, 'ro')
plt.xlabel("effectif total des candidats ")
plt.ylabel("taux d'acces (en %)")
plt.axis()

plt.show()

# 2eme nuage de point

plt.plot(rang_dernier_appele_groupe1, taux_acces, 'ro')
plt.xlabel("rang du dernier appeler du groupe 1")
plt.ylabel("taux d'acces (en %)")
plt.axis()

plt.show()


# 3eme nuage de point

plt.plot(departement_code, taux_acces, 'ro')
plt.xlabel("Code de département")
plt.ylabel("taux d'acces (en %)")
plt.axis([0, 100, 0, 100])

plt.show()