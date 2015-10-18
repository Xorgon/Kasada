import pygame
import shiplayer


class Ship(pygame.sprite.Group):
    r = [0, 0]
    v = [0, 0]
    a = [0, 0]

    name = "default"

    outer = None
    inner = None
    collide = None

    rect = None

    main = None

    def __init__(self, main):
        self.main = main
        self.outer = shiplayer.ShipLayer(pygame.image.load(self.name + "/outer.png"), self)
        self.inner = shiplayer.ShipLayer(pygame.image.load(self.name + "/inner.png"), self)
        self.collide = shiplayer.ShipLayer(pygame.image.load(self.name + "/collide.png"), self)

    def update_vects(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]

        self.r[0] += self.v[0]
        self.r[1] += self.v[1]

    def set_rect(self):
        p_r = self.main.player.r
        self.rect.x = self.r[0] - p_r[0]
        self.rect.y = self.r[1] - p_r[1]

        self.outer.rect = self.rect
        self.inner.rect = self.rect
        self.collide.rect = self.rect