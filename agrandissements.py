import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from transformations import AgrandissementOrigine

xtriangle = np.array([1, 1.5, 1.25])
ytriangle = np.array([1, 1, 1.5])

N = 90
fig = plt.figure()
plt.axis('equal')

scale_total = 2.0
liste_images = []

for j in range(N+1):
    v = AgrandissementOrigine(1 + (scale_total - 1) * j / N, xtriangle, ytriangle)
    [xi, yi] = v
    im = plt.fill(xi, yi, facecolor='none', edgecolor='blue') \
       + plt.plot(xi, yi, 'ro') \
       + plt.plot(0, 0, 'go')
    liste_images.append(im)

anim = animation.ArtistAnimation(fig, liste_images)
anim.save("AgrandissementTriangle.gif", writer="pillow", fps=30)
