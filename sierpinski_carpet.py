
from turtle import *

def carre (x, y, longueur):
    up()
    goto(x, y)
    down()
    begin_fill()

    for i in range(4):
        forward(longueur) 
        left(90) 
    
    end_fill()

def carre_enfant(x,y,longueur):
    return [carre_est(x, y, longueur),
            carre_nord_est(x, y, longueur),
            carre_nord(x, y, longueur),
            carre_nord_ouest(x, y, longueur),
            carre_ouest(x, y, longueur),
            carre_sud_ouest(x, y, longueur),
            carre_sud(x, y, longueur),
            carre_sud_est(x, y, longueur)]

def carre_est(x, y, longueur):
    return x + 4 * longueur // 3, y + longueur // 3 , longueur // 3

def carre_nord_est(x, y, longueur):
    return x + 4 * longueur // 3, y + 4 * longueur // 3, longueur // 3

def carre_nord(x, y, longueur):
    return x + longueur // 3, y + 4 * longueur // 3, longueur // 3

def carre_nord_ouest(x, y, longueur):
    return x - 2 * longueur // 3, y + 4 * longueur // 3, longueur // 3

def carre_ouest(x, y, longueur):
    return x - 2 * longueur // 3, y + longueur // 3, longueur // 3

def carre_sud_ouest(x, y, longueur):
    return x - 2 * longueur // 3, y - 2 * longueur // 3, longueur // 3

def carre_sud(x, y, longueur):
    return x + longueur // 3, y - 2 * longueur // 3, longueur // 3

def carre_sud_est(x, y, longueur):
    return x + 4 * longueur // 3, y - 2 * longueur // 3, longueur // 3


def test_carre(x,y,longueur):
    carre(x, y, longueur)

speed = 3
clear()
carre(150, -150, 243)


for x,y,longueur in carre_enfant(150,-150,243):
    test_carre(x,y,longueur)

done()



