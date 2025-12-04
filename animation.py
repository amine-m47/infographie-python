import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import cos, sin, pi

# Fonction de rotation autour d'un point A
def Rotation(A, t, x, y):
    xA, yA = A
    X = np.array(x) - xA
    Y = np.array(y) - yA
    Xr = X * cos(t) - Y * sin(t)
    Yr = X * sin(t) + Y * cos(t)
    return Xr + xA, Yr + yA

# Fonction pour créer un cercle
def create_circle(x, y, radius, num_points=100):
    theta = np.linspace(0, 2*np.pi, num_points)
    x_circle = x + radius * np.cos(theta)
    y_circle = y + radius * np.sin(theta)
    return x_circle, y_circle

# Configuration de la figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_facecolor('white')  # Fond blanc pour un meilleur contraste

# Liste pour stocker les images de l'animation
liste_images = []

# Coordonnées initiales des formes (dispersées)
# Triangle 1 (oreille gauche)
x_triangle1 = np.array([0.5, 1, 0.75])
y_triangle1 = np.array([2.5, 2.5, 3])

# Triangle 2 (oreille droite)
x_triangle2 = np.array([2.5, 3, 2.75])
y_triangle2 = np.array([2.5, 2.5, 3])

# Cercle 1 (tête)
x_circle1, y_circle1 = create_circle(1.5, 2, 0.75)

# Cercles pour les yeux
left_eye = create_circle(1.2, 2.2, 0.2)
right_eye = create_circle(1.8, 2.2, 0.2)

# Cercles pour les pupilles
left_pupil = create_circle(1.2, 2.2, 0.05)
right_pupil = create_circle(1.8, 2.2, 0.05)

# Cercle pour le nez
x_nose, y_nose = create_circle(1.5, 1.75, 0.1)

# Lignes pour les moustaches
x_moustache1 = [1.5, 1.0, 1.5]  # Moustache gauche
y_moustache1 = [1.75, 1.85, 1.65]
x_moustache2 = [1.5, 2.0, 1.5]  # Moustache droite
y_moustache2 = [1.75, 1.85, 1.65]
x_moustache3 = [1.5, 1.2, 1.5]  # Moustache gauche 2
y_moustache3 = [1.75, 1.95, 1.55]
x_moustache4 = [1.5, 1.8, 1.5]  # Moustache droite 2
y_moustache4 = [1.75, 1.95, 1.55]

# Lignes pour la bouche
x_mouth = [1.3, 1.7, 1.5]  # Bouche
y_mouth = [1.5, 1.5, 1.4]

# Création des images pour chaque étape de l'animation
for j in range(101):  # 101 étapes pour une rotation complète
    angle = 2 * pi * j / 100  # Angle de rotation (0 à 2π)

    # Transformation des triangles (oreilles)
    # Déplacer les triangles vers le centre
    tx1 = 1.0 - np.mean(x_triangle1)
    ty1 = 2.75 - np.mean(y_triangle1)
    x_triangle1_translated = [x + tx1 * j / 100 for x in x_triangle1]
    y_triangle1_translated = [y + ty1 * j / 100 for y in y_triangle1]

    tx2 = 2.0 - np.mean(x_triangle2)
    ty2 = 2.75 - np.mean(y_triangle2)
    x_triangle2_translated = [x + tx2 * j / 100 for x in x_triangle2]
    y_triangle2_translated = [y + ty2 * j / 100 for y in y_triangle2]

    # Rotation des triangles
    xi1, yi1 = Rotation((1.0, 2.75), angle, x_triangle1_translated, y_triangle1_translated)
    xi2, yi2 = Rotation((2.0, 2.75), angle, x_triangle2_translated, y_triangle2_translated)

    # Transformation des cercles (yeux et nez)
    tx_circle1 = 1.5 - 1.5
    ty_circle1 = 2 - 2
    x_circle1_translated = [x + tx_circle1 * j / 100 for x in x_circle1]
    y_circle1_translated = [y + ty_circle1 * j / 100 for y in y_circle1]

    tx_left_eye = 1.2 - 1.2
    ty_left_eye = 2.2 - 2.2
    x_left_eye_translated = [x + tx_left_eye * j / 100 for x in left_eye[0]]
    y_left_eye_translated = [y + ty_left_eye * j / 100 for y in left_eye[1]]

    tx_right_eye = 1.8 - 1.8
    ty_right_eye = 2.2 - 2.2
    x_right_eye_translated = [x + tx_right_eye * j / 100 for x in right_eye[0]]
    y_right_eye_translated = [y + ty_right_eye * j / 100 for y in right_eye[1]]

    tx_left_pupil = 1.2 - 1.2
    ty_left_pupil = 2.2 - 2.2
    x_left_pupil_translated = [x + tx_left_pupil * j / 100 for x in left_pupil[0]]
    y_left_pupil_translated = [y + ty_left_pupil * j / 100 for y in left_pupil[1]]

    tx_right_pupil = 1.8 - 1.8
    ty_right_pupil = 2.2 - 2.2
    x_right_pupil_translated = [x + tx_right_pupil * j / 100 for x in right_pupil[0]]
    y_right_pupil_translated = [y + ty_right_pupil * j / 100 for y in right_pupil[1]]

    tx_nose = 1.5 - 1.5
    ty_nose = 1.75 - 1.75
    x_nose_translated = [x + tx_nose * j / 100 for x in x_nose]
    y_nose_translated = [y + ty_nose * j / 100 for y in y_nose]

    # Transformation des moustaches
    tx_moustache1 = 1.5 - 1.5
    ty_moustache1 = 1.75 - 1.75
    x_moustache1_translated = [x + tx_moustache1 * j / 100 for x in x_moustache1]
    y_moustache1_translated = [y + ty_moustache1 * j / 100 for y in y_moustache1]

    tx_moustache2 = 1.5 - 1.5
    ty_moustache2 = 1.75 - 1.75
    x_moustache2_translated = [x + tx_moustache2 * j / 100 for x in x_moustache2]
    y_moustache2_translated = [y + ty_moustache2 * j / 100 for y in y_moustache2]

    tx_moustache3 = 1.5 - 1.5
    ty_moustache3 = 1.75 - 1.75
    x_moustache3_translated = [x + tx_moustache3 * j / 100 for x in x_moustache3]
    y_moustache3_translated = [y + ty_moustache3 * j / 100 for y in y_moustache3]

    tx_moustache4 = 1.5 - 1.5
    ty_moustache4 = 1.75 - 1.75
    x_moustache4_translated = [x + tx_moustache4 * j / 100 for x in x_moustache4]
    y_moustache4_translated = [y + ty_moustache4 * j / 100 for y in y_moustache4]

    # Transformation de la bouche
    tx_mouth = 1.5 - 1.5
    ty_mouth = 1.5 - 1.5
    x_mouth_translated = [x + tx_mouth * j / 100 for x in x_mouth]
    y_mouth_translated = [y + ty_mouth * j / 100 for y in y_mouth]

    # Dessiner les triangles (oreilles)
    im1 = ax.fill(xi1, yi1, facecolor='pink', edgecolor='black')
    im2 = ax.fill(xi2, yi2, facecolor='pink', edgecolor='black')

    # Dessiner le cercle (tête)
    im3 = ax.plot(x_circle1_translated, y_circle1_translated, color='orange', linewidth=2)

    # Dessiner les yeux
    im4 = ax.fill(x_left_eye_translated, y_left_eye_translated, facecolor='white', edgecolor='black')
    im5 = ax.fill(x_right_eye_translated, y_right_eye_translated, facecolor='white', edgecolor='black')

    # Dessiner les pupilles
    im6 = ax.fill(x_left_pupil_translated, y_left_pupil_translated, facecolor='black')
    im7 = ax.fill(x_right_pupil_translated, y_right_pupil_translated, facecolor='black')

    # Dessiner le nez
    im8 = ax.fill(x_nose_translated, y_nose_translated, facecolor='pink')

    # Dessiner les moustaches
    im9 = ax.plot(x_moustache1_translated, y_moustache1_translated, color='black', linewidth=1)
    im10 = ax.plot(x_moustache2_translated, y_moustache2_translated, color='black', linewidth=1)
    im11 = ax.plot(x_moustache3_translated, y_moustache3_translated, color='black', linewidth=1)
    im12 = ax.plot(x_moustache4_translated, y_moustache4_translated, color='black', linewidth=1)

    # Dessiner la bouche
    im13 = ax.plot(x_mouth_translated, y_mouth_translated, color='black', linewidth=1)

    # Ajouter les éléments graphiques à la liste
    liste_images.append(im1 + im2 + im3 + im4 + im5 + im6 + im7 + im8 + im9 + im10 + im11 + im12 + im13)

# Création de l'animation
anim = animation.ArtistAnimation(fig, liste_images, interval=50)

# Sauvegarder l'animation en GIF
anim.save("animation_chat.gif", writer="pillow", fps=30)

# Afficher l'animation
plt.show()
