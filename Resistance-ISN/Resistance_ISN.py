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

#Définition Fonction

def Couleurs():
	global Resis
	Resis = ZT.get()
	strResis = list(str(Resis))

	if strResis[0] == "0":
		Graphique.itemconfig(RB1, fill = noir)
	if strResis[0] == "1":
		Graphique.itemconfig(RB1, fill = marron)
	if strResis[0] == "2":
		Graphique.itemconfig(RB1, fill = rouge)
	if strResis[0] == "3":
		Graphique.itemconfig(RB1, fill = orange)
	if strResis[0] == "4":
		Graphique.itemconfig(RB1, fill = jaune)
	if strResis[0] == "5":
		Graphique.itemconfig(RB1, fill = vert)
	if strResis[0] == "6":
		Graphique.itemconfig(RB1, fill = bleu)
	if strResis[0] == "7":
		Graphique.itemconfig(RB1, fill = violet)
	if strResis[0] == "8":
		Graphique.itemconfig(RB1, fill = gris)
	if strResis[0] == "9":
		Graphique.itemconfig(RB1, fill = blanc)

	if strResis[1] == "0":
		Graphique.itemconfig(RB2, fill = noir)
	if strResis[1] == "1":
		Graphique.itemconfig(RB2, fill = marron)
	if strResis[1] == "2":
		Graphique.itemconfig(RB2, fill = rouge)
	if strResis[1] == "3":
		Graphique.itemconfig(RB2, fill = orange)
	if strResis[1] == "4":
		Graphique.itemconfig(RB2, fill = jaune)
	if strResis[1] == "5":
		Graphique.itemconfig(RB2, fill = vert)
	if strResis[1] == "6":
		Graphique.itemconfig(RB2, fill = bleu)
	if strResis[1] == "7":
		Graphique.itemconfig(RB2, fill = violet)
	if strResis[1] == "8":
		Graphique.itemconfig(RB2, fill = gris)
	if strResis[1] == "9":
		Graphique.itemconfig(RB2, fill = blanc)

	if strResis[2] == "0":
		Graphique.itemconfig(RB3, fill = noir)
	if strResis[2] == "1":
		Graphique.itemconfig(RB3, fill = marron)
	if strResis[2] == "2":
		Graphique.itemconfig(RB3, fill = rouge)
	if strResis[2] == "3":
		Graphique.itemconfig(RB3, fill = orange)
	if strResis[2] == "4":
		Graphique.itemconfig(RB3, fill = jaune)
	if strResis[2] == "5":
		Graphique.itemconfig(RB3, fill = vert)
	if strResis[2] == "6":
		Graphique.itemconfig(RB3, fill = bleu)
	if strResis[2] == "7":
		Graphique.itemconfig(RB3, fill = violet)
	if strResis[2] == "8":
		Graphique.itemconfig(RB3, fill = gris)
	if strResis[2] == "9":
		Graphique.itemconfig(RB3, fill = blanc)

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
RB1 = Graphique.create_rectangle(260, 180, 360, 540, fill = blanc)
RB2 = Graphique.create_rectangle(410, 180, 510, 540, fill = blanc)
RB3 = Graphique.create_rectangle(560, 180, 660, 540, fill = blanc)

#Création Bande Multiplicateur
RBM = Graphique.create_rectangle(920, 180, 1020, 540, fill = blanc)

#Initialisation du GUI
Fenetre.mainloop()


