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

RB = [0, 1, 2, 3]

#Définition Fonction

def Couleurs():
	strResis = list(str(ZT.get()))
	for I in range(4):
		if I == 3 and len(str(ZT.get())) > 3:
			strResis[I] = str(len(ZT.get()) - 3)
		if I ==3 and len(str(ZT.get())) <= 3:
			Graphique.itemconfig(RB[I], fill = noir)
			break;
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


def Clean():
	for I in range(4):
		Graphique.itemconfig(RB[I], fill = blanc)
	ZT.delete(first = 0, last = len(str(ZT.get())))

#Création Fenètre
Fenetre = Tk()
Fenetre.title('Résistance')

#Création du Canvas
Graphique = Canvas(Fenetre, width = 1280, height = 720, bg = blanc)
Graphique.pack()

#Création Bouton Quitter
BoutonQuitter = Button(Fenetre, text = 'Quitter', command = Fenetre.destroy)
BoutonQuitter.pack(side = RIGHT, padx = 5, pady = 5)

#Création Zone de Texte
ZT = Entry()
ZT.focus_set()
ZT.pack(side = LEFT, fill = BOTH) #Il faut le centrer entre les 2 boutons

#Création Bouton Afficher
BoutonAfficher = Button(Fenetre, text = 'Afficher', command = Couleurs)
BoutonAfficher.pack(side = LEFT, padx = 5, pady = 5)

#Création Bouton Effacer
BoutonEffacer = Button(Fenetre, text = 'Effacer', command = Clean)
BoutonEffacer.pack(side = LEFT)

#Création Rectangle Central
RC = Graphique.create_rectangle(160, 180, 1120, 540, outline = noir , fill = '#87591A')

#Création Lignes
LN = Graphique.create_line(20, 360, 160 , 360, width = 20)
LN2 = Graphique.create_line(1120, 360, 1260, 360, width = 20)

#Création Bandes
RB[0] = Graphique.create_rectangle(260, 180, 360, 540, fill = blanc)
RB[1] = Graphique.create_rectangle(410, 180, 510, 540, fill = blanc)
RB[2] = Graphique.create_rectangle(560, 180, 660, 540, fill = blanc)

#Création Bande Multiplicateur
RB[3] = Graphique.create_rectangle(920, 180, 1020, 540, fill = blanc)

#Initialisation du GUI
Fenetre.mainloop()


