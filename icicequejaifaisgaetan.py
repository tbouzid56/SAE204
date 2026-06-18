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
liste_boites = [taux_acces, departement_code, effectif_total_candidats]
plt.boxplot(liste_boites)
plt.show()

# 2eme Boites a moustaches 
liste_boites2 = [taux_acces, effectif_total_candidats]
plt.boxplot(liste_boites2)
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

import numpy.linalg as la

# Régression linéaire multiple

# Filtrer les lignes contenant un nan (un nan est toujours différent de lui-même)
taux_liste = []
rang_liste = []
effectif_liste = []
departement_liste = []

for i in range(len(taux_acces)):
    t = float(taux_acces[i])
    r = float(rang_dernier_appele_groupe1[i])
    e = float(effectif_total_candidats[i])
    d = float(departement_code[i])
    if t == t and r == r and e == e and d == d:
        taux_liste.append(t)
        rang_liste.append(r)
        effectif_liste.append(e)
        departement_liste.append(d)

Y = np.array(taux_liste)
n = len(Y)
uns = np.ones(n)
X = np.array([uns, rang_liste, effectif_liste, departement_liste]).T

M = X.T @ X
V = X.T @ Y
A = la.solve(M, V)

b  = A[0]
a1 = A[1]
a2 = A[2]
a3 = A[3]

print("b  =", b)
print("a1 =", a1)
print("a2 =", a2)
print("a3 =", a3)