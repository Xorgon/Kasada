import pygame
import util.collisions


class Player(pygame.sprite.DirtySprite):
    r = [800, 300]
    v = [0, 0]
    a = [0, 0]

    offset = [500, 325]

    hit = False

    main = None

    def __init__(self, main, group):
        pygame.sprite.Sprite.__init__(self)
        self.main = main
        self.image = pygame.image.load("images/basechar.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_bounding_rect()
        self.rect.x = self.offset[0]
        self.rect.y = self.offset[1]
        self.add(group)

    def update_vects(self):
        self.r[0] += self.v[0]
        self.r[1] += self.v[1]

        self.v[0] += self.a[0]
        self.v[1] += self.a[1]

    def ship_collide(self, ship):
        x = ship.r[0] - self.r[0]
        y = ship.r[1] - self.r[1]
        col = self.mask.overlap_area(ship.collide.mask, (int(x), int(y)))
        if col != 0:
            self.a[1] = 0
            offset = util.collisions.get_collision_vect(self, ship.collide)
            self.r[0] += offset[0]
            self.r[1] += offset[1]
        return col
