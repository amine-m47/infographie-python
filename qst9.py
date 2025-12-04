import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi, cos, sin
from transformations import Rotation2

# --- Triangle de base ---
xtriangle = np.array([1, 1.5, 1.25])
ytriangle = np.array([1, 1, 1.5])

# Sommet autour duquel on tourne
A = (xtriangle[0], ytriangle[0])

# Nombre d'images
N = 90

fig = plt.figure()
plt.axis('equal')

liste_images = []

for j in range(N+1):
    # Calcul de l'angle pour cette image
    angle = 2 * pi * j / N  # rotation complète sur N images
    xr, yr = Rotation2(A, angle, xtriangle, ytriangle)

    # Tracé du triangle et du sommet
    im = plt.fill(xr, yr, facecolor='none', edgecolor='blue') \
       + plt.plot(xr, yr, 'ro') \
       + plt.plot(A[0], A[1], 'go')  # sommet autour duquel on tourne
    liste_images.append(im)

# Création de l'animation
anim = animation.ArtistAnimation(fig, liste_images)
anim.save("RotationTriangle.gif", writer="pillow", fps=30)
