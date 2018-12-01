from tkinter import *
import webbrowser
from tkinter.messagebox import *

#Définition des variables

RB = [0, 1, 2, 3]

#Définition des Couleurs (PC = Palette de Couleurs)
#Dans l'ordre: noir, marron, rouge, orange, jaune, vert, bleu, violet, gris, blanc
PC = ['#000000', '#582900', '#FF0000', 'orange', 'yellow', '#00FF00', '#0000FF', 'violet', 'grey', '#FFFFFF']


#Définition Fonctions

#Fonction de vérification s'il n'y a pas de nombres décimaux et nombres > 10^9
def Verification():
	point = 0
	for I in range(len(str(ZT.get()))):
		if str(ZT.get())[I] == ".":
			point = 1
			break;
	if len(str(ZT.get())) > 10 or point == 1:
		WARN = showwarning("Attention!", "Je digère mal les nombres décimaux et les nombres au dessus de 10^9. Veuillez vérifier votre saisie")
	else:
		Couleurs()

#Fonction de coloration des bandes
def Couleurs():
	strResis = str(ZT.get())
	Clean()
	if len(strResis) <= 3:
		for I in range(len(strResis)):
			Graphique.itemconfig(RB[I], fill = PC[int(strResis[I])])
	else:
		for I in range(3):
			Graphique.itemconfig(RB[I], fill = PC[int(strResis[I])])
	Graphique.itemconfig(RB[3], fill = PC[len(strResis)-1])
	Resis.set('Voici les couleurs de la résistance pour: ' + strResis)

#Fonction "Quand on appuie sur "enter""
def Enter(event):
	Verification()

#Fonction de nettoyage
def Clean():
	for I in range(4):
		Graphique.itemconfig(RB[I], fill = PC[0])
	ZT.delete(first = 0, last = len(str(ZT.get())))
	Resis.set("<--- Veuillez saisir votre résistance")

#Fonction Ouvrir la page du projet
def Web():
	webbrowser.open_new_tab('https://github.com/Frederic94500/Resistance-ISN')


#Création Fenètre
Fenetre = Tk()
Fenetre.title('Résistance')

#Création du Canvas
Graphique = Canvas(Fenetre, width = 1280, height = 720, bg = PC[9])
Graphique.pack()

#Création barre de menu
menubar = Menu(Fenetre)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Fichier", menu = filemenu)
filemenu.add_command(label = "Quitter", command = Fenetre.destroy)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Aide", menu = helpmenu)
helpmenu.add_command(label = "Vistez le GitHub", command = Web)

Fenetre.config(menu=menubar)

#Création Bouton Afficher
BoutonAfficher = Button(Fenetre, text = 'Afficher', command = Verification)
BoutonAfficher.pack(side = LEFT, padx = 5, pady = 5)

#Création Bouton Effacer
BoutonEffacer = Button(Fenetre, text = 'Effacer', command = Clean)
BoutonEffacer.pack(side = LEFT)

#Création Zone de Texte
ZT = Entry(justify = CENTER)
ZT.focus_set()
ZT.pack(side = LEFT, fill = BOTH, padx = 5, pady = 5)

#Quand on appuie sur "enter"
Fenetre.bind('<Return>', Enter)

#Création Texte
Resis = StringVar()
TA = Label(Fenetre, textvariable = Resis)
Resis.set("<--- Veuillez saisir votre résistance")
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