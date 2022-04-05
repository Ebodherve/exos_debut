from turtle import *

def carre(taille, couleur,angle):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    color(couleur)
    c =0
    while c <4:
        forward(taille)
        right(angle)
        c = c +1

def triangle(taille, couleur,angle):
    "fonction qui dessine un triangle de taille et de couleur déterminées"
    color(couleur)
    c =0
    while c <3:
        forward(taille)
        right(angle)
        c = c +1

def etoile5(taille,couleur,angle):
    "fonction qui dessine un etoile de taille et de couleur déterminées"
    color(couleur)
    c =0
    while c <5:
        forward(taille)
        right(angle)
        c = c +1



