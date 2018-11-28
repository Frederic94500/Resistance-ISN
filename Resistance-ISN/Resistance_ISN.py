from tkinter import *

#Définition des variables

rouge = '#FF0000'
bleu = '#0000FF'
vert = '#00FF00'
orange = 'orange'
jaune = 'yellow'
violet = 'violet'
gris = 'grey'
blanc = '#FFFFFF'
noir = '#000000'

Resis = 0

CB1 = blanc
CB2 = blanc
CB3 = blanc
CBM = blanc

def Couleurs():
	global CB1
	global CB2
	global CB3
	global CBM
	global Resis
	for I in range(3):
		if Resis.get[0] == "0":
			Graphique.itemconfig(RB1, fill=noir)



#Création Fenètre
Fenetre = Tk()
Fenetre.title('Résistance')

#Création du Canvas
Graphique = Canvas(Fenetre, width = 1280, height = 720, bg = blanc)
Graphique.pack()

#Création Bouton Quitter
BoutonQuitter = Button(Fenetre, text ='Quitter', command = Fenetre.destroy)
BoutonQuitter.pack(side = RIGHT, padx = 5, pady = 5)

#Création Zone de Texte
Resis = StringVar()
ZT = Entry(Fenetre, textvariable = Resis)
ZT.focus_set()
ZT.pack() #Il faut le centrer entre les 2 boutons

#Création Bouton Afficher
BoutonAfficher = Button(Fenetre, text ='Afficher', command = Couleurs)
BoutonAfficher.pack(side = LEFT, padx = 5, pady = 5)

#Création Rectangle Central
RC = Graphique.create_rectangle(160, 180, 1120, 540, outline = noir , fill = blanc)

#Création Lignes
LN = Graphique.create_line(20, 360, 160 , 360)
LN2 = Graphique.create_line(1120, 360, 1260, 360)

#Création Bandes
RB1 = Graphique.create_rectangle(260, 180, 360, 540, fill = CB1)
#RB2 = Graphique.create_rectangle(410, 180, 510, 540, fill = CB2)
#RB3 = Graphique.create_rectangle(560, 180, 660, 540, fill = CB3)

#Création Bande Multiplicateur
#RBM = Graphique.create_rectangle(920, 180, 1020, 540, bg = CBM)

#Initialisation du GUI
Fenetre.mainloop()


