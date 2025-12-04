import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import cos, sin, pi

# Fonction de rotation autour d'un point A
def Rotation(A, t, x, y):
    xA, yA = A
    X, Y = x - xA, y - yA  # Translation pour centrer sur A
    Xr = X * cos(t) - Y * sin(t)  # Rotation
    Yr = X * sin(t) + Y * cos(t)  # Rotation
    return Xr + xA, Yr + yA  # Translation inverse

# Coordonnées du triangle (exemple : un triangle simple)
xtriangle = np.array([1, 1.5, 1.25])
ytriangle = np.array([1, 1, 1.5])

# Configuration de la figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

# Liste pour stocker les images de l'animation
liste_images = []

# Point autour duquel on fait tourner le triangle (ici, le premier sommet)
A = [xtriangle[0], ytriangle[0]]

# Création des images pour chaque étape de l'animation
for j in range(101):  # 101 étapes pour une rotation complète
    angle = 2 * pi * j / 100  # Angle de rotation (0 à 2π)
    xi, yi = Rotation(A, angle, xtriangle, ytriangle)

    # Dessiner le triangle
    im1 = ax.fill(xi, yi, facecolor='none', edgecolor='green')
    im2 = ax.plot(xi, yi, 'ro')  # Points du triangle en rouge
    im3 = ax.plot(A[0], A[1], 'bo', markersize=10)  # Point A en bleu

    # Ajouter les éléments graphiques à la liste
    liste_images.append(im1 + im2 + im3)

# Création de l'animation
anim = animation.ArtistAnimation(fig, liste_images, interval=50)

# Sauvegarder l'animation en GIF
anim.save("RotationTriangle.gif", writer="pillow", fps=30)

# Afficher l'animation
plt.show()
