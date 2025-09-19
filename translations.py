import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from transformations import TranslationOrigine

xtriangle = np.array([1, 1.5, 1.25])
ytriangle = np.array([1, 1, 1.5])

N = 100
fig = plt.figure()
plt.axis('equal')
plt.xlim(-1, 5)
plt.ylim(-1, 5)

dx_total, dy_total = 3, 2
liste_images = []

for j in range(N+1):
    dx = dx_total * j / N
    dy = dy_total * j / N

    v = TranslationOrigine(xtriangle, ytriangle, dx, dy)
    [xi, yi] = v

    im = (plt.fill(xi, yi, facecolor='none', edgecolor='purple')
          + plt.plot(xi, yi, 'ro')
          + plt.plot(0, 0, 'go'))
    liste_images.append(im)

anim = animation.ArtistAnimation(fig, liste_images)
anim.save("Translation.gif", writer="pillow", fps=30)
