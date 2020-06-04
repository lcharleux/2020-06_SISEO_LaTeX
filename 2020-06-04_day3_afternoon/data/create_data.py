import numpy as np #Librairie qui gère des matrices etc...
from matplotlib import pyplot as plt  # Librairie pour les graphiques
import pandas as pd # Librairie pour les données tabulaires, les stats etc...

# ON CREE DES DONNEES
x = np.linspace(0., 10., 21) # Valeurs de x entre 0 et 10 avec 20 points équirépartis
y =  np.exp(-x/10) * np.sin(2. * np.pi * x / 5)

# ON LES STOCKE DANS UN TABLEAU
data = pd.DataFrame()
data["x"] = x # On ajoute une colonne "x"
data["y"] = y

# SAUVEGARDE DU TABLEAU
data.to_csv("data.csv", index = False)