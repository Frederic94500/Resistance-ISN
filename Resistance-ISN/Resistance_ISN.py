# -*- encoding: utf-8 -*-
#Frédéric94500 - Résistance-ISN

from tkinter import *
import webbrowser
from tkinter.messagebox import *
from PIL import Image, ImageTk

#Définition des variables
RectangleBande = [0, 1, 2, 3]
ChiffresSignificatif = 3

#PHrase de début
PHStart = "<--- Veuillez saisir la valeur de votre résistance"

#Définition des Couleurs (PC = Palette de Couleurs)
#Dans l'ordre: noir, marron, rouge, orange, jaune, vert, bleu, violet, gris, blanc
PC = ['#000000', '#582900', '#FF0000', 'orange', 'yellow', '#00FF00', '#0000FF', 'violet', 'grey', '#FFFFFF']


#Définition des Fonctions
#Fonction de vérification s'il y a que des chiffres, de > 12 et de nombres < ChiffresSignificatif
def Verification():
	global listResis
	try:
		test = int(ZoneTexte.get()) #Vérifie s'il y a des caractères étrangés, s'il y a: passe vers except ValueError
		listResis = list(str(test))
		for I in range(len(listResis)): #Supprime les zéros
			if listResis[I] == "0": del listResis[0:0]
			else: break;
		if (ChiffresSignificatif == 3 and len(listResis) < 3) or (ChiffresSignificatif == 2 and len(listResis) < 2): #Vérifie s'il y a peu de ChiffresSignificatif
			WARN = showwarning("Attention!", "Votre valeur " + "".join(listResis) + " n'a pas assez de chiffres significatifs (c'est-à-dire " + str(ChiffresSignificatif) + "). Veuillez vérifier votre saisie.")
			Texte.set('<--- Veuillez vérifier votre valeur')
			return
		if len(listResis) > 12: #Vérifie s'il y a trop de chiffres
			WARN = showwarning("Attention!", "Je digère mal les nombres au dessus de 12 chiffres significatifs! Veuillez vérifier votre saisie.")
			Texte.set('<--- Veuillez vérifier votre valeur')
			return
		else: Couleurs(ChiffresSignificatif)

	except ValueError:
		WARN = showwarning("Attention!", "Je n'accepte que des chiffres! Veuillez vérifier votre saisie.")
		Texte.set('<--- Veuillez vérifier votre valeur')
		return

#Fonction de coloration des bandes
def Couleurs(ChiffresSignificatif):
	Clean()
	Texte.set('Voici les couleurs de la résistance pour: ' + "".join(listResis))
	[Graphique.itemconfig(RectangleBande[I], fill = PC[int(listResis[I])]) for I in range(ChiffresSignificatif)]
	del listResis[0:ChiffresSignificatif-1]
	Graphique.itemconfig(RectangleBande[3], fill = PC[len(listResis)-1])
		
#Fonction "Quand on appuie sur "enter""
def Enter(event):
	Verification()

#Fonction de nettoyage
def Clean():
	if ChiffresSignificatif == 3: [Graphique.itemconfig(RectangleBande[I], fill = PC[0]) for I in range(4)]
	else:
		[Graphique.itemconfig(RectangleBande[I], fill = PC[0]) for I in range(ChiffresSignificatif)]
		Graphique.itemconfig(RectangleBande[3], fill = PC[0])
	ZoneTexte.delete(first = 0, last = len(str(ZoneTexte.get())))
	Texte.set(PHStart)

#Fonction du choix du nombres de bandes selon les chiffres significatifs
def Bandes3():
	global ChiffresSignificatif
	Graphique.itemconfig(RectangleBande[2], fill = "#87591A", outline = "#87591A")
	ChiffresSignificatif = 2
	Fenetre.title("Résistance à 3 bandes")
	Clean()

def Bandes4():
	global ChiffresSignificatif
	Graphique.itemconfig(RectangleBande[2], fill = PC[0], outline = PC[0])
	ChiffresSignificatif = 3
	Fenetre.title("Résistance à 4 bandes")
	Clean()

#Fonctions d'ouverture de pages web
def WebProj():
	webbrowser.open_new_tab('https://github.com/Frederic94500/Resistance-ISN')

def WebAuteur(event):
	webbrowser.open_new_tab('https://twitter.com/Frederic94500')

def WebLicence(event):
	webbrowser.open_new_tab('https://github.com/Frederic94500/Resistance-ISN/blob/master/LICENSE')

#Fonction à propos (créateur + licence)(ouvre une nouvelle fenêtre)
def APropos():
	About = Toplevel()
	About.title("A propos et licence")

	AbText = [0, 1, 2, 3]

	AbText[0] = Label(About, text = "Ce programme a été fait par")
	AbText[1] = Label(About, text = "Frédéric94500", fg = "blue", cursor = "hand2")
	AbText[2] = Label(About, text = "sous la licence")
	AbText[3] = Label(About, text = "GPL-3.0", fg = "blue", cursor = "hand2")

	AbText[1].bind("<Button-1>", WebAuteur)
	AbText[3].bind("<Button-1>", WebLicence)

	[AbText[I].pack(side = "left", pady = 10) for I in range(4)]

	photo = ImageTk.PhotoImage(Image.open("gpl.png"))
	img = Label(About, image=photo)
	img.image = photo
	img.pack()

	About.iconbitmap('icon.ico')


#Création Fenètre
Fenetre = Tk()
Fenetre.title('Résistance à 4 bandes')
Fenetre.iconbitmap('icon.ico')

#Création du Canvas
Graphique = Canvas(Fenetre, width = 1280, height = 480, bg = PC[9])
Graphique.pack()

#Création barre de menu
menubar = Menu(Fenetre)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Fichier", menu = filemenu)
filemenu.add_command(label = "Quitter", command = Fenetre.destroy)

Actif = IntVar()
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edition", menu = editmenu)
editmenu.add_command(label = "Effacer la résistance", command = Clean)
editmenu.add_separator()
editmenu.add_radiobutton(label = "Résistance à 4 bandes", variable = Actif, value = 0, command = Bandes4)
editmenu.add_radiobutton(label = "Résistance à 3 bandes", variable = Actif, value = 1, command = Bandes3)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Aide", menu = helpmenu)
helpmenu.add_command(label = "Vistez le GitHub", command = WebProj)
helpmenu.add_separator()
helpmenu.add_command(label = "A propos et licence", command = APropos)

Fenetre.config(menu=menubar)

#Création Bouton Afficher
BoutonAfficher = Button(Fenetre, text = 'Afficher', command = Verification).pack(side = LEFT, padx = 5, pady = 5)

#Création Bouton Effacer
BoutonEffacer = Button(Fenetre, text = 'Effacer', command = Clean).pack(side = LEFT)

#Création Zone de Texte
ZoneTexte = Entry(justify = CENTER)
ZoneTexte.focus_set()
ZoneTexte.pack(side = LEFT, fill = BOTH, padx = 5, pady = 5)

#Quand on appuie sur "enter"
Fenetre.bind('<Return>', Enter)

#Création Texte et Texte Annonce
Texte = StringVar()
TextAnnonce = Label(Fenetre, textvariable = Texte).pack(side = LEFT)
Texte.set(PHStart)

#Création Rectangle Central
RC = Graphique.create_rectangle(160, 120, 1120, 360, outline = '#87591A' , fill = '#87591A')

#Création Connecteurs
Connecteur = Graphique.create_line(20, 240, 160 , 240, width = 20)
Connecteur2 = Graphique.create_line(1120, 240, 1260, 240, width = 20)

#Création Rectangles Bandes
RectangleBande[0] = Graphique.create_rectangle(260, 120, 360, 360, fill = PC[0])
RectangleBande[1] = Graphique.create_rectangle(410, 120, 510, 360, fill = PC[0])

#Création Rectangle Bande variable (disparaît à 2 Chiffres Significatifs)
RectangleBande[2] = Graphique.create_rectangle(560, 120, 660, 360, fill = PC[0])

#Création Rectangle Bande Multiplicateur
RectangleBande[3] = Graphique.create_rectangle(920, 120, 1020, 360, fill = PC[0])

#Initialisation du GUI
Fenetre.mainloop()