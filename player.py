import pygame


class Player(pygame.sprite.DirtySprite):
    r = [0, 0]
    v = [0, 0]
    a = [0, 0]

    main = None

    def __init__(self, main):
        self.main = main

    def update_vects(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]

        self.r[0] += self.v[0]
        self.r[1] += self.v[1]
