import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.linalg as la

# importer le csv dans le python
df_formation =  pd.read_csv("export_csv.csv", sep=";") # sep pour preciser le séparateur
# test pour voir si c'est bien dans la variable
#print(df_formation.head())
#print(df_formation.columns)



# Passer ensuite en numpy.array les données de df_num_lannion :
arr_formation = df_formation.to_numpy() 
# print(arr_formation)

# verif ligne par ligne de si oui ou non y a une valeur null
lignes_avec_nan = np.isnan(arr_formation).any(axis=1)

# pour supprimer les lignes avec une valeur null (le ~ c'est pour tous garder sauf ce que y a dans lignes avec nan)
arr_formation_propre = arr_formation[~lignes_avec_nan]
print(arr_formation_propre)

taux_acces = arr_formation_propre[:,0]
# print(taux_acces)


rang_dernier_appele_groupe1 = arr_formation_propre[:,1]
#print(rang_dernier_appele_groupe1)


effectif_total_candidats = arr_formation_propre[:,2]
#print(effectif_total_candidats)

departement_code = arr_formation_propre[:,3]
#print(departement_code)



# Boites a moustaches 
# liste_boites = [taux_acces, departement_code, effectif_total_candidats]
# plt.boxplot(liste_boites)
# plt.show()

# 2eme Boites a moustaches 
liste_boites2 = [taux_acces, effectif_total_candidats]
plt.boxplot(liste_boites2)
plt.show()


# 3eme Boites a moustaches 
liste_boites2 = [taux_acces, departement_code]
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



# Régression linéaire 

nb_lignes = len(taux_acces)

# initialiser X
X = np.zeros((nb_lignes, 4))


# ajout collone par collone
X[:, 0] = np.ones(nb_lignes)                  
X[:, 1] = rang_dernier_appele_groupe1
X[:, 2] = effectif_total_candidats 
X[:, 3] = departement_code 

# crétion de la matrice Y
Y = np.array(taux_acces)

# transposer de X
tX = X.T

# Résultat de produit matriciel entre la transpose de X et X
M = tX @ X

# Matrice inverce de la matrice M
M2 = la.inv(M)

# Résultat de produit matriciel entre la transpose de X et Y
N = tX @ Y

# Calcule de la Matrice A
A = M2 @ N

# Affichage de la matrice A
print(A)

# Affichage de la régretion linéaire
print("Taux d'acces prédit = ", A[1] ," x rang_dernier_appele + ", A[2]," x effectif_total + ", A[3]," x code_departement + ",A[0])

# Fonction pour calculer le taux d'accès prédit par ligne 
def pred_taux_acces(i): #pour i je met le num de la ligne propre dcp, plutot que mettre toutes les valeurs à la mano...
    return A[1]*rang_dernier_appele_groupe1[i] + A[2]*effectif_total_candidats[i] + A[3]*departement_code[i] + A[0]


# Calcule de l'erreur au carré (taux acces)
def erreur_carre(i) :
    return ((pred_taux_acces(i) - arr_formation_propre[i])**2)

# Calcule de l'erreur moyenne 
nb_ligne_propre = len(arr_formation_propre)
def erreur_moyenne() :
    a = 0
    for i in range(nb_ligne_propre):
        a = a + erreur_carre(i)
    return a / nb_ligne_propre



