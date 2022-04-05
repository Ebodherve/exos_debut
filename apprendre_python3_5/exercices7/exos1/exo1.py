from turtle import *

def triangle(couleur,cote) :
	color(couleur)
	for i in range(3) :
		forward(cote)
		left(120)


def ltriangle(cote) :
	palette = ["blue","red","green","gray","yellow"]
	for couleur in palette :
		triangle(couleur,cote)
		up()
		forward(cote+10)
		down()


ltriangle(50)
input()


