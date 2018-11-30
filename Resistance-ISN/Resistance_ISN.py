from tkinter import *

#Définition des variables

RB = [0, 1, 2, 3]

Resis = 0

#Définition des Couleurs (PC = Palette de Couleurs)
#Dans l'ordre: noir, marron, rouge, orange, jaune, vert, bleu, violet, gris, blanc
PC = ['#000000', '#582900', '#FF0000', 'orange', 'yellow', '#00FF00', '#0000FF', 'violet', 'grey', '#FFFFFF']


#Définition Fonctions
#Fonction de coloration des bandes
def Couleurs():
	global strResis
	strResis = str(ZT.get())
	Clean()
	Info()
	if len(strResis) <= 3:
		for I in range(len(strResis)):
			Graphique.itemconfig(RB[I], fill = PC[int(strResis[I])])
	else:
		for I in range(3):
			Graphique.itemconfig(RB[I], fill = PC[int(strResis[I])])
	Graphique.itemconfig(RB[3], fill = PC[len(strResis)-1])

#Fonction de nettoyage
def Clean():
	for I in range(4):
		Graphique.itemconfig(RB[I], fill = PC[0])
	ZT.delete(first = 0, last = len(str(ZT.get())))
	Resis.set("")

#Fonction d'affichage pour la couleur du résistance
def Info():
	Resis.set('Voici les couleurs du résistance pour: ' + strResis)


#Création Fenètre
Fenetre = Tk()
Fenetre.title('Résistance')

#Création du Canvas
Graphique = Canvas(Fenetre, width = 1280, height = 720, bg = PC[9])
Graphique.pack()

#Création Bouton Quitter
BoutonQuitter = Button(Fenetre, text = 'Quitter', command = Fenetre.destroy)
BoutonQuitter.pack(side = RIGHT, padx = 5, pady = 5)

#Création Zone de Texte
ZT = Entry(justify = CENTER)
ZT.focus_set()
ZT.pack(side = LEFT, fill = BOTH)

#Création Bouton Afficher
BoutonAfficher = Button(Fenetre, text = 'Afficher', command = Couleurs)
BoutonAfficher.pack(side = LEFT, padx = 5, pady = 5)

#Création Bouton Effacer
BoutonEffacer = Button(Fenetre, text = 'Effacer', command = Clean)
BoutonEffacer.pack(side = LEFT)

#Création Texte
#Texte annonce nombre
Resis = StringVar()
TA = Label(Fenetre, textvariable = Resis)
TA.pack()

#Création Rectangle Central
RC = Graphique.create_rectangle(160, 180, 1120, 540, outline = PC[0] , fill = '#87591A')

#Création Lignes
LN = Graphique.create_line(20, 360, 160 , 360, width = 20)
LN2 = Graphique.create_line(1120, 360, 1260, 360, width = 20)

#Création Bandes
RB[0] = Graphique.create_rectangle(260, 180, 360, 540, fill = PC[0])
RB[1] = Graphique.create_rectangle(410, 180, 510, 540, fill = PC[0])
RB[2] = Graphique.create_rectangle(560, 180, 660, 540, fill = PC[0])

#Création Bande Multiplicateur
RB[3] = Graphique.create_rectangle(920, 180, 1020, 540, fill = PC[0])

#Initialisation du GUI
Fenetre.mainloop()


