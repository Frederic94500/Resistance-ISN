from tkinter import *

#Création Fenètre
Fenetre = Tk()
Fenetre.title('Résistance')

#Création du Canvas
Graphique = Canvas(Fenetre, width = 1280, height = 720, bg = '#FFFFFF')
Graphique.pack()

#Création Bouton Quitter
BoutonQuitter = Button(Fenetre, text ='Quitter', command = Fenetre.destroy)
BoutonQuitter.pack()

#Création Bouton Afficher
BoutonQuitter = Button(Fenetre, text ='Afficher') #command = Fenetre.destroy)
BoutonQuitter.pack()

#Création Rectangle Central
RC = Graphique.create_rectangle(160, 180, 1120, 540, outline='black', fill='#FFFFFF')

#Création Lignes
LN = Graphique.create_line(20, 360, 160 , 360)
LN2 = Graphique.create_line(1120, 360, 1260, 360)

#Création Bandes


Fenetre.mainloop()