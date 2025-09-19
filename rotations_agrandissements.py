import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from transformations import RotationOrigine, AgrandissementOrigine

xtriangle = np.array([1, 1.5, 1.25])
ytriangle = np.array([1, 1, 1.5])

N = 90
fig = plt.figure()
plt.axis('equal')

angle_total = pi/2
scale_total = 2.0
liste_images = []

for j in range(N+1):
    angle = angle_total * j / N
    scale = 1 + (scale_total - 1) * j / N

    v = RotationOrigine(angle, xtriangle, ytriangle)
    v = AgrandissementOrigine(scale, v[0], v[1])

    [xi, yi] = v
    im = plt.fill(xi, yi, facecolor='none', edgecolor='red') \
       + plt.plot(xi, yi, 'bo') \
       + plt.plot(0, 0, 'go')
    liste_images.append(im)

anim = animation.ArtistAnimation(fig, liste_images)
anim.save("RotationAgrandissementTriangle.gif", writer="pillow", fps=30)
