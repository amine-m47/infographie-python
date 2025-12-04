import numpy as np
from math import cos, sin

def RotationOrigine(t, x, y):
    # Rotation d’angle t (radians) autour de l’origine
    # avec x les points abscisses et y les points des
    # ordonnées de la figure
    M = np.array([[cos(t), -sin(t)], [sin(t), cos(t)]])
    v = np.array([x, y])
    return M.dot(v)

def Rotation(A, t, x, y):
    # Rotation d’angle t (radians) autour du point A
    # avec x les points abscisses et y les points des
    # ordonnées de la figure
    xa, ya = A
    X = x -xa
    Y = y -ya
    M = np.array([[cos(t), -sin(t)], [sin(t), cos(t)]])
    v = np.array([X, Y])
    Xr, Yr = M.dot(v)
    return Xr + xa, Yr + ya

def AgrandissementOrigine(l, x, y):
    # Homothétie de rapport l autour de l’origine
    # avec x les points abscisses et y les points
    # des ordonnées de la figure
    M = np.array([[l, 0], [0, l]])
    v = np.array([x, y])
    return M.dot(v)

def TranslationOrigine(x, y, tx, ty):
    # Translation de  avec
    # x les points abscisses et y les points
    # des ordonnées de la figure
    v = np.array([x, y])
    t = np.array([[tx], [ty]])
    return v + t

def Rotation2(A, t, x, y):
    xa, ya = A

    X = x - xa
    Y = y - ya
    M = np.array([[cos(t), -sin(t)],
                  [sin(t),  cos(t)]])
    pts = np.vstack((X, Y))
    Xr, Yr = np.dot(M, pts)
    return Xr + xa, Yr + ya
