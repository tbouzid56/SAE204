import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.linalg as la
#----------------------------------------------------------------------
# PARTIE A
# importer le csv dans le python
df_formation =  pd.read_csv("export_csv.csv", sep=";") 


arr_formation = df_formation.to_numpy() 


# Enlever les valeurs null
lignes_avec_nan = np.isnan(arr_formation).any(axis=1)
arr_formation_propre = arr_formation[~lignes_avec_nan]

# Creation des variables
taux_acces = arr_formation_propre[:,0]
rang_dernier_appele_groupe1 = arr_formation_propre[:,1]
effectif_total_candidats = arr_formation_propre[:,2]
departement_code = arr_formation_propre[:,3]


#----------------------------------------------------------------------
# PARTIE B
# Boites a moustaches  
liste_boites1 = [taux_acces, effectif_total_candidats]
plt.boxplot(liste_boites1)
plt.show()


liste_boites2 = [taux_acces, departement_code]
plt.boxplot(liste_boites2)
plt.show()




# Nuage de points
plt.plot(effectif_total_candidats, taux_acces, 'ro')
plt.xlabel("effectif total des candidats ")
plt.ylabel("taux d'acces (en %)")
plt.axis()
plt.show()


plt.plot(rang_dernier_appele_groupe1, taux_acces, 'ro')
plt.xlabel("rang du dernier appeler du groupe 1")
plt.ylabel("taux d'acces (en %)")
plt.axis()
plt.show()


plt.plot(departement_code, taux_acces, 'ro')
plt.xlabel("Code de département")
plt.ylabel("taux d'acces (en %)")
plt.axis([0, 100, 0, 100])
plt.show()


#----------------------------------------------------------------------
# PARTIE C
# Régression linéaire 

nb_lignes = len(taux_acces)

# Crétion de la matrice X
X = np.zeros((nb_lignes, 4))

X[:, 0] = np.ones(nb_lignes)                  
X[:, 1] = rang_dernier_appele_groupe1
X[:, 2] = effectif_total_candidats 
X[:, 3] = departement_code 

# Crétion de la matrice Y
Y = np.array(taux_acces)

tX = X.T

M = tX @ X

M2 = la.inv(M)

N = tX @ Y

A = M2 @ N

# Affichage de la régretion linéaire
print("Taux d'acces prédit = ", A[1] ," x rang_dernier_appele + ", A[2]," x effectif_total + ", A[3]," x code_departement + ",A[0])


#----------------------------------------------------------------------
# PARTIE D (Plus difficile)


def pred_taux_acces(i): 
    return A[1]*rang_dernier_appele_groupe1[i] + A[2]*effectif_total_candidats[i] + A[3]*departement_code[i] + A[0]


def erreur_carre(i) :
    return ((pred_taux_acces(i) - arr_formation_propre[i][0])**2)


nb_ligne_propre = len(arr_formation_propre)
def erreur_moyenne() :
    a = 0
    for i in range(nb_ligne_propre):
        a = a + erreur_carre(i)
    return a / nb_ligne_propre  


def Moyenne(Y) :
    return sum(Y) / len(Y)

def Variance(Y):
    m = Moyenne(Y)
    somme = 0

    for i in range(len(Y)):
        somme = somme + (Y[i] - m)**2

    return somme / len(Y)

def Cor(Y) :
    return ((1 - (erreur_moyenne() / Variance(Y)))**0.5)

print(Cor(taux_acces))
