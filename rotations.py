import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi
from transformations import RotationOrigine

xtriangle = np.array([1, 1.5, 1.25])
ytriangle = np.array([1, 1, 1.5])

N = 150
fig = plt.figure()
plt.axis('equal')

angle_total = 2 * pi
liste_images = []

for j in range(N+1):
    v = RotationOrigine(angle_total * j / N, xtriangle, ytriangle)
    [xi, yi] = v
    im = plt.fill(xi, yi, facecolor='none', edgecolor='red') \
       + plt.plot(xi, yi, 'bo') \
       + plt.plot(0, 0, 'go')
    liste_images.append(im)

anim = animation.ArtistAnimation(fig, liste_images)
anim.save("RotationTriangle.gif", writer="pillow", fps=30)
