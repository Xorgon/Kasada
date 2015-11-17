import pygame


class ShipLayer(pygame.sprite.DirtySprite):

    r = [0, 0]
    v = [0, 0]
    a = [0, 0]

    ship = None

    def __init__(self, image, ship):

        self.dirty = 2
        self.blendmode = 0
        self.visible = 1
        self.source_rect = pygame.Rect(0, 0, 1000, 1000)

        self.r = ship.r
        self.v = ship.v
        self.a = ship.a

        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.mask = pygame.mask.from_surface(image)
        self.rect = self.image.get_rect()
        self.ship = ship
