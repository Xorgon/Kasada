import pygame


class ShipLayer(pygame.sprite.DirtySprite):
    ship = None

    def __init__(self, image, ship):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.mask = image
        self.rect = self.image.get_rect()
        self.add(ship)
        self.ship = ship
