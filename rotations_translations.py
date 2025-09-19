import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi
from transformations import RotationOrigine, TranslationOrigine

# Triangle
xtriangle = np.array([1, 1.5, 1.25])
ytriangle = np.array([1, 1, 1.5])

# Animation
N = 100
fig = plt.figure()
plt.axis('equal')

angle_total = 2 * pi
dx_total, dy_total = 2, 1
liste_images = []

for j in range(N+1):
    angle = angle_total * j / N
    dx = dx_total * j / N
    dy = dy_total * j / N

    v = RotationOrigine(angle, xtriangle, ytriangle)
    v = TranslationOrigine(v[0], v[1], dx, dy)

    [xi, yi] = v
    im = plt.fill(xi, yi, facecolor='none', edgecolor='green') \
       + plt.plot(xi, yi, 'ro') \
       + plt.plot(0, 0, 'go')
    liste_images.append(im)

anim = animation.ArtistAnimation(fig, liste_images)
anim.save("RotationTranslationTriangle.gif", writer="pillow", fps=30)
