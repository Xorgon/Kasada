import pygame
import shiplayer


class Ship(pygame.sprite.LayeredDirty):
    r = [500, 250]
    v = [0, 0]
    a = [0, 0]

    name = "default"

    outer = None
    inner = None
    collide = None

    rect = None

    main = None

    def __init__(self, main):
        pygame.sprite.LayeredDirty.__init__(self)
        self.main = main

        self.inner = shiplayer.ShipLayer(pygame.image.load("images/" + self.name + "/inner.png"), self)
        self.collide = shiplayer.ShipLayer(pygame.image.load("images/" + self.name + "/collide.png"), self)
        self.outer = shiplayer.ShipLayer(pygame.image.load("images/" + self.name + "/outer.png"), self)

        self.add(self.inner)
        self.add(self.collide)
        self.add(self.outer)

        self.move_to_front(self.outer)
        self.move_to_back(self.inner)
        self.set_rect()

    def update_vects(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]

        self.r[0] += self.v[0]
        self.r[1] += self.v[1]

        for layer in (self.outer, self.inner, self.collide):
            layer.r = self.r
            layer.v = self.v
            layer.a = self.a

    def set_rect(self):
        if self.rect is None:
            self.rect = self.outer.image.get_bounding_rect()
        p = self.main.player
        self.rect.x = self.r[0] - p.r[0] + p.offset[0]
        self.rect.y = self.r[1] - p.r[1] + p.offset[1]

        self.outer.rect = self.rect
        self.inner.rect = self.rect
        self.collide.rect = self.rect
