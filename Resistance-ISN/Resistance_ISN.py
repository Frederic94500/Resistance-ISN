from tkinter import *

#Définition des variables

noir = '#000000'
marron = '#582900'
rouge = '#FF0000'
orange = 'orange'
jaune = 'yellow'
vert = '#00FF00'
bleu = '#0000FF'
violet = 'violet'
gris = 'grey'
blanc = '#FFFFFF'

Resis = 0

RB = [0, 1, 2]

#Définition Fonction

def Couleurs():
	global Resis
	Resis = ZT.get()
	strResis = list(str(Resis))
	for I in range(3):
		if strResis[I] == "0":
			Graphique.itemconfig(RB[I], fill = noir)
		if strResis[I] == "1":
			Graphique.itemconfig(RB[I], fill = marron)
		if strResis[I] == "2":
			Graphique.itemconfig(RB[I], fill = rouge)
		if strResis[I] == "3":
			Graphique.itemconfig(RB[I], fill = orange)
		if strResis[I] == "4":
			Graphique.itemconfig(RB[I], fill = jaune)
		if strResis[I] == "5":
			Graphique.itemconfig(RB[I], fill = vert)
		if strResis[I] == "6":
			Graphique.itemconfig(RB[I], fill = bleu)
		if strResis[I] == "7":
			Graphique.itemconfig(RB[I], fill = violet)
		if strResis[I] == "8":
			Graphique.itemconfig(RB[I], fill = gris)
		if strResis[I] == "9":
			Graphique.itemconfig(RB[I], fill = blanc)

	nbCM = len(Resis) - 3

	if nbCM == 0:
		Graphique.itemconfig(RBM, fill = noir)
	if nbCM == 1:
		Graphique.itemconfig(RBM, fill = marron)
	if nbCM == 2:
		Graphique.itemconfig(RBM, fill = rouge)
	if nbCM == 3:
		Graphique.itemconfig(RBM, fill = orange)
	if nbCM == 4:
		Graphique.itemconfig(RBM, fill = jaune)
	if nbCM == 5:
		Graphique.itemconfig(RBM, fill = vert)
	if nbCM == 6:
		Graphique.itemconfig(RBM, fill = bleu)
	if nbCM == 7:
		Graphique.itemconfig(RBM, fill = violet)
	if nbCM == 8:
		Graphique.itemconfig(RBM, fill = gris)
	if nbCM == 9:
		Graphique.itemconfig(RBM, fill = blanc)


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
ZT = Entry()
ZT.focus_set()
ZT.pack(side = RIGHT, fill = BOTH) #Il faut le centrer entre les 2 boutons

#Création Bouton Afficher
BoutonAfficher = Button(Fenetre, text ='Afficher', command = Couleurs)
BoutonAfficher.pack(side = LEFT, padx = 5, pady = 5)

#Création Rectangle Central
RC = Graphique.create_rectangle(160, 180, 1120, 540, outline = noir , fill = '#87591A')

#Création Lignes
LN = Graphique.create_line(20, 360, 160 , 360)
LN2 = Graphique.create_line(1120, 360, 1260, 360)

#Création Bandes
RB[0] = Graphique.create_rectangle(260, 180, 360, 540, fill = blanc)
RB[1] = Graphique.create_rectangle(410, 180, 510, 540, fill = blanc)
RB[2] = Graphique.create_rectangle(560, 180, 660, 540, fill = blanc)

#Création Bande Multiplicateur
RBM = Graphique.create_rectangle(920, 180, 1020, 540, fill = blanc)

#Initialisation du GUI
Fenetre.mainloop()


