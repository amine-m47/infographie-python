import matplotlib

matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, Polygon


# ---------------------------------------------------------
# Fonctions utilitaires
# ---------------------------------------------------------
def create_triangle(center, size, upright=True):
    if upright:
        base_x = np.array([0, size, size / 2])
        base_y = np.array([0, 0, size])
    else:
        base_x = np.array([0, size, size / 2])
        base_y = np.array([size, size, 0])
    x = base_x - size / 2
    y = base_y
    # appliquer rotation si nécessaire et décaler au centre
    return np.column_stack([x + center[0], y + center[1]])


def rotate_triangle(triangle_points, angle_deg, center):
    angle = np.deg2rad(angle_deg)
    cx, cy = center
    rotated = []
    for x, y in triangle_points:
        xr = np.cos(angle) * (x - cx) - np.sin(angle) * (y - cy) + cx
        yr = np.sin(angle) * (x - cx) + np.cos(angle) * (y - cy) + cy
        rotated.append([xr, yr])
    return np.array(rotated)


# ---------------------------------------------------------
# Figure
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_aspect('equal')

# Tête
head = Circle((2, 2), 1.2, facecolor='none', edgecolor='black', lw=1.5)
ax.add_patch(head)

# Oreilles animées
ear_size = 0.7
ear_left_final_center = np.array([1.25, 3.1])
ear_right_final_center = np.array([2.75, 3.1])

# Oreilles départ (aléatoires)
ear_left_center_start = np.random.uniform(0, 4, 2)
ear_right_center_start = np.random.uniform(0, 4, 2)
ear_left_angle_start = np.random.uniform(-90, 90)  # rotation initiale
ear_right_angle_start = np.random.uniform(-90, 90)

# Créer les triangles au départ
ear_left_tri = create_triangle(ear_left_center_start, ear_size, True)
ear_right_tri = create_triangle(ear_right_center_start, ear_size, True)
ear_left = Polygon(rotate_triangle(ear_left_tri, ear_left_angle_start, ear_left_center_start), facecolor='none',
                   edgecolor='black', lw=1.5)
ear_right = Polygon(rotate_triangle(ear_right_tri, ear_right_angle_start, ear_right_center_start), facecolor='none',
                    edgecolor='black', lw=1.5)
ax.add_patch(ear_left)
ax.add_patch(ear_right)

# Yeux
eye_left = Circle((1.55, 2.4), 0.0, facecolor='none', edgecolor='black', lw=1.5)
eye_right = Circle((2.45, 2.4), 0.0, facecolor='none', edgecolor='black', lw=1.5)
ax.add_patch(eye_left)
ax.add_patch(eye_right)

# Pupilles
pupil_left = Circle((1.55, 2.4), 0.0, facecolor='black')
pupil_right = Circle((2.45, 2.4), 0.0, facecolor='black')
ax.add_patch(pupil_left)
ax.add_patch(pupil_right)

# Nez
nose = Polygon(create_triangle((2, 1.9), 0.2, upright=False), facecolor='black', alpha=0.0)
ax.add_patch(nose)

# Moustaches
moustache_angles = [-30, -15, 15, 30, 150, 165, 195, 210]
moustaches = []
for angle in moustache_angles:
    cx, cy = 2, 1.9
    rad = np.deg2rad(angle)
    x = np.array([cx, cx + 0.8 * np.cos(rad)])
    y = np.array([cy, cy + 0.8 * np.sin(rad)])
    line, = ax.plot([x[0], x[0]], [y[0], y[0]], 'k', lw=1.5)
    moustaches.append((line, x, y))

# ---------------------------------------------------------
# Animation
NB_FRAMES = 150


def update(frame):
    t = frame / (NB_FRAMES - 1)

    # Oreilles : translation + rotation
    new_left_center = ear_left_center_start + (ear_left_final_center - ear_left_center_start) * t
    new_right_center = ear_right_center_start + (ear_right_final_center - ear_right_center_start) * t
    new_left_angle = ear_left_angle_start * (1 - t)
    new_right_angle = ear_right_angle_start * (1 - t)
    ear_left.set_xy(rotate_triangle(create_triangle(new_left_center, ear_size, True), new_left_angle, new_left_center))
    ear_right.set_xy(
        rotate_triangle(create_triangle(new_right_center, ear_size, True), new_right_angle, new_right_center))

    # Tête
    head.set_radius(1.2 * t)

    # Yeux
    if t > 0.3:
        eye_left.set_radius(0.2 * (t - 0.3) / 0.7)
        eye_right.set_radius(0.2 * (t - 0.3) / 0.7)

    # Pupilles
    if t > 0.5:
        pupil_left.set_radius(0.1 * (t - 0.5) / 0.5)
        pupil_right.set_radius(0.1 * (t - 0.5) / 0.5)

    # Nez
    if t > 0.6:
        nose.set_alpha((t - 0.6) / 0.4)

    # Moustaches
    for line, x, y in moustaches:
        appear_t = 0.7
        progress = max(0, (t - appear_t) / (1 - appear_t))
        x_end = x[0] + (x[1] - x[0]) * progress
        y_end = y[0] + (y[1] - y[0]) * progress
        line.set_data([x[0], x_end], [y[0], y_end])

    return [head, ear_left, ear_right, eye_left, eye_right, pupil_left, pupil_right, nose] + [l[0] for l in moustaches]


anim = FuncAnimation(fig, update, frames=NB_FRAMES, blit=True)
anim.save("Tete_Chat_Oreilles_Rotation.gif", writer='pillow', fps=25)

print("GIF généré ✔ : oreilles avec translation + rotation, triangles non déformés")
