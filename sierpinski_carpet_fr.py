from turtle import *

def carre(x, y, longueur):
    """Dessine un carré plein à la position x, y avec une certaine longueur."""
    up()
    goto(x, y)
    down()
    begin_fill()
    for _ in range(4):
        forward(longueur)
        left(90)
    end_fill()

def carre_enfant(x, y, longueur):
    """ Retourne la liste des 8 sous-carrés autour du centre """
    return [
        (x + 2 * longueur // 3, y + longueur // 3, longueur // 3),  # Est
        (x + 2 * longueur // 3, y + 2 * longueur // 3, longueur // 3),  # Nord-Est
        (x + longueur // 3, y + 2 * longueur // 3, longueur // 3),  # Nord
        (x, y + 2 * longueur // 3, longueur // 3),  # Nord-Ouest
        (x, y + longueur // 3, longueur // 3),  # Ouest
        (x, y, longueur // 3),  # Sud-Ouest
        (x + longueur // 3, y, longueur // 3),  # Sud
        (x + 2 * longueur // 3, y, longueur // 3),  # Sud-Est
    ]

def sierpinski(x, y, longueur, profondeur):
    """ Dessine le tapis de Sierpiński """
    if profondeur == 0:
        carre(x, y, longueur)
    else:
        # On ignore le centre et on fait appel récursivement sur les 8 autres zones
        for (nx, ny, nl) in carre_enfant(x, y, longueur):
            sierpinski(nx, ny, nl, profondeur - 1)

# Initialisation
bgcolor("white")
color("black", "black")
speed(10)        # Choisi la vitesse de dessin de la tortue
tracer(5)        

# Démarrer le dessin
longueur_initiale = 243
profondeur = 4
sierpinski(-longueur_initiale // 2, -longueur_initiale // 2, longueur_initiale, profondeur)

update()
done()
