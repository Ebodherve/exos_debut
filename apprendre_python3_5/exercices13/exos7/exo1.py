from tkinter import *

def cercle(can, x, y, r,color = "gray"):
    "dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
    can.create_oval(x-r, y-r, x+r, y+r,fill = color)

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        # constructeur de la classe parente
        self.can =Canvas(self, width =475, height =130, bg ="white")
        self.can.pack(side =TOP, padx =5, pady =5)
        Button(self, text ="Train", command =self.dessine).pack(side =LEFT)
        Button(self, text ="Hello", command =self.coucou).pack(side =LEFT)
        Button(self, text ="Allumer", command =self.allumage).pack(side =LEFT)
    def dessine(self):
        "instanciation de 4 wagons dans le canevas"
        self.w1 = Wagon(self.can,  10, 30)
        self.w2 = Wagon(self.can, 130, 30)
        self.w3 = Wagon(self.can, 250, 30)
        self.w4 = Wagon(self.can, 370, 30)
    def coucou(self):
        try :
            "apparition de personnages dans certaines fenêtres"
            self.w1.perso(3)        # 1er wagon, 3e fenêtre
            self.w3.perso(1)        # 3e wagon, 1e fenêtre
            self.w3.perso(2)        # 3e wagon, 2e fenêtre
            self.w4.perso(1)        # 4e wagon, 1e fenêtre
        except :
            pass
    def allumage(self):
        try :
            "allumage des wagons"
            self.w1.allumer()
            self.w2.allumer()
            self.w3.allumer()
            self.w4.allumer()
        except :
            pass

class Wagon(object):
    def __init__(self, canev, x, y,couleur = "orange",fen = 1):
        "dessin d'un petit wagon en <x,y> dans le canevas <canev>"
        self.fen = fen
        # mémorisation des paramètres dans des variables d'instance :
        self.canev, self.x, self.y = canev, x, y
        # rectangle de base : 95x60 pixels :
        canev.create_rectangle(x, y, x+95, y+60,fill = couleur)
        # 3 fenêtres de 25x40 pixels, écartées de 5 pixels :
        for xf in range(x+5, x+90, 30):
            canev.create_rectangle(xf, y+5, xf+25, y+40,fill = "black")
            # 2 roues de rayon égal à 12 pixels :
        cercle(canev, x+18, y+73, 12)
        cercle(canev, x+77, y+73, 12)
    def perso(self, fen = 1,col = "brown"):
        "apparition d'un petit personnage à la fenêtre <fen>"
        # calcul des coordonnées du centre de chaque fenêtre :
        self.fen = fen
        xf = self.x + self.fen*30 -12
        yf = self.y + 25
        cercle(self.canev, xf, yf, 10,color= col)        # visage
        cercle(self.canev, xf-5, yf-3, 2,color= col)        # oeil gauche
        cercle(self.canev, xf+5, yf-3, 2,color= col)        # oeil droit
        cercle(self.canev, xf, yf+5, 3,color= col)        # bouche
    def allumer(self):
        for xf in range(self.x+5, self.x+90, 30):
            self.canev.create_rectangle(xf, self.y+5, xf+25, self.y+40,fill = "yellow")
        xf = self.x + self.fen*30 -12
        yf = self.y + 25
        cercle(self.canev, xf, yf, 10,color= "pink")
        cercle(self.canev, xf-5, yf-3, 2,color= "black")
        cercle(self.canev, xf+5, yf-3, 2,color= "black")
        cercle(self.canev, xf, yf+5, 3,color= "black")

app = Application()
app.mainloop()


