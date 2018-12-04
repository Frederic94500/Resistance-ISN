from tkinter import *
import webbrowser
from tkinter.messagebox import *

#Définition des variables

RB = [0, 1, 2, 3]
global ChiffresSigni

#PHrase de début
PHStart = "<--- Veuillez saisir la valeur de votre résistance"

#Définition des Couleurs (PC = Palette de Couleurs)
#Dans l'ordre: noir, marron, rouge, orange, jaune, vert, bleu, violet, gris, blanc
PC = ['#000000', '#582900', '#FF0000', 'orange', 'yellow', '#00FF00', '#0000FF', 'violet', 'grey', '#FFFFFF']


#Définition Fonctions

#Fonction de vérification s'il n'y a pas de nombres décimaux et nombres > 10^9
def Verification():
	global strResis
	global ChiffresSigni
	strResis = list(str(ZT.get()))
	point = 0
	for I in range(len(strResis)):
		if strResis[I] == "." or strResis[I] == " ":
			point = 1
			break;
	if len(strResis) > 10 or point == 1:
		WARN = showwarning("Attention!", "Je digère mal les nombres décimaux, les espaces et les nombres au dessus de 10^9. Veuillez vérifier votre saisie")
		Resis.set('<--- Veuillez vérifier votre valeur')
	else:
		Couleurs(ChiffresSigni)

#Fonction de coloration des bandes
def Couleurs(ChiffresSigni):
	#Clean()
	Resis.set('Voici les couleurs de la résistance pour: ' + "".join(strResis))
	for I in range(ChiffresSigni):
		Graphique.itemconfig(RB[I], fill = PC[int(strResis[I])])
	del strResis[0:ChiffresSigni-1]
	Graphique.itemconfig(RB[3], fill = PC[len(strResis)-1])


#Fonction "Quand on appuie sur "enter""
def Enter(event):
	Verification()

#Fonction de nettoyage
def Clean():
	for I in range(4):
		Graphique.itemconfig(RB[I], fill = PC[0])
	ZT.delete(first = 0, last = len(str(ZT.get())))
	Resis.set(PHStart)

#Fonction du choix du nombres de bandes
def Bandes4():
	Graphique.itemconfig(RB[2], fill = PC[0], outline = PC[0])
	ChiffresSigni = 3

def Bandes3():
	Graphique.itemconfig(RB[2], fill = "#87591A", outline = "#87591A")
	ChiffresSigni = 2

#Fonction Ouvrir la page du projet
def Web():
	webbrowser.open_new_tab('https://github.com/Frederic94500/Resistance-ISN')


#Création Fenètre
Fenetre = Tk()
Fenetre.title('Résistance')

#Création du Canvas
Graphique = Canvas(Fenetre, width = 1280, height = 480, bg = PC[9])
Graphique.pack()

#Création barre de menu
menubar = Menu(Fenetre)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Fichier", menu = filemenu)
filemenu.add_command(label = "Quitter", command = Fenetre.destroy)

Actif = IntVar()
ChiffresSigni = 3
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edition", menu = editmenu)
editmenu.add_radiobutton(label = "Résistance à 4 bandes", variable = Actif, value = 0, command = Bandes4)
editmenu.add_radiobutton(label = "Résistance à 3 bandes", variable = Actif, value = 1, command = Bandes3)

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
Resis.set(PHStart)
TA.pack()

#Création Rectangle Central
RC = Graphique.create_rectangle(160, 120, 1120, 360, outline = PC[0] , fill = '#87591A')

#Création Lignes
LN = Graphique.create_line(20, 240, 160 , 240, width = 20)
LN2 = Graphique.create_line(1120, 240, 1260, 240, width = 20)

#Création Rectangles Bandes
RB[0] = Graphique.create_rectangle(260, 120, 360, 360, fill = PC[0])
RB[1] = Graphique.create_rectangle(410, 120, 510, 360, fill = PC[0])
RB[2] = Graphique.create_rectangle(560, 120, 660, 360, fill = PC[0])

#Création Bande Multiplicateur
RB[3] = Graphique.create_rectangle(920, 120, 1020, 360, fill = PC[0])

#Initialisation du GUI
Fenetre.mainloop()