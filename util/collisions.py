import pygame
import math


def get_collision_vect(obj1, obj2):
    x = obj2.r[0] - obj1.r[0]
    y = obj2.r[1] - obj1.r[1]

    a1 = obj1.mask.overlap_area(obj2.mask, (int(x + 1), int(y)))
    a2 = obj1.mask.overlap_area(obj2.mask, (int(x - 1), int(y)))
    dx = a1 - a2
    a3 = obj1.mask.overlap_area(obj2.mask, (int(x), int(y + 1)))
    a4 = obj1.mask.overlap_area(obj2.mask, (int(x), int(y - 1)))
    dy = a3 - a4

    mag = (dx ** 2 + dy ** 2) ** 0.5

    print("dx=" + str(dx))

    if mag > 0:
        ny = dy / mag
        nx = dx / mag
    else:
        ny = 0
        nx = 0

    cont = True
    k = 1
    while cont:
        area = obj1.mask.overlap_area(obj2.mask, (int(x - k * nx), int(y - k * ny)))
        if area == 0:
            cont = False
            k_nx = k * nx
            k_ny = k * ny
            ox = k_nx
            oy = k_ny
            if k_nx < 1:
                ox = int(math.floor(k_nx))
            else:
                ox = int(math.ceil(k_nx))
            if k_ny < 1:
                oy = int(math.floor(k_ny))
            else:
                oy = int(math.ceil(k_ny))
            return ox, oy
        else:
            k += 1
