# TRACE D'UNE FIGURE AVEC MATPLOTLIB

import numpy as np #Librairie qui gère des matrices etc...
from matplotlib import pyplot as plt  # Librairie pour les graphiques
import pandas as pd # Librairie pour les données tabulaires, les stats etc...


#-------------------------------------------------------------------------------
# FIGURE CONFIGURATION
import matplotlib as mpl
from rcparams import RCPARAMS
mpl.use("pgf")
mpl.rcParams.update(RCPARAMS)
width = 6.69        # fig width in inches
height = width /2.5 # fig heigth in inches
#-------------------------------------------------------------------------------



# CHARGEMENT DES DONNEES
data = pd.read_csv("data.csv")

# # AFFICHAGE DE LA FIGURE
# width = 6.69        # fig width in inches (source doc Elsevier sur les figures)
# height = width / 2.5 # fig heigth in inches


fig = plt.figure(figsize = (width, height)) # ON CREE UN ESPACE DE DESSIN
plt.plot(data.x, # VALEURS X
         data.y, # VALEURS Y
         marker = "o", 
         color = "b")
plt.grid()
plt.xlabel("Temps $t$ [s]")
plt.ylabel("Amplitude $a$ [V]")
plt.title(r"Fonction $a(t) = \exp(\frac{b}{t}) \sin(2\pi c t)$")
plt.tight_layout() # Attention a ce que rien ne déborde
plt.savefig("fig_python.pdf", 
            bbox_inches='tight') # SAUVEGARDE LA FIGURE EN PDF

import os
os.system("pdfcrop fig_python.pdf fig_python.pdf")

# SMALL VERSION
fig.set_figwidth(width / 2)
fig.set_figheight(height)
plt.tight_layout() # Attention a ce que rien ne déborde
plt.savefig("fig_python_small.pdf", 
            bbox_inches='tight') # SAUVEGARDE LA FIGURE EN PDF
#plt.show()
plt.close("all")
os.system("pdfcrop fig_python_small.pdf fig_python_small.pdf")
