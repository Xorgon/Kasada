import pygame


class Player(pygame.sprite.DirtySprite):
    r = [500, 250]
    v = [0, 0]
    a = [0, 0]

    main = None

    def __init__(self, main, group):
        pygame.sprite.Sprite.__init__(self)
        self.main = main
        self.image = pygame.image.load("images/basechar.png")
        self.rect = pygame.Rect(self.r[0], self.r[1], 100, 100)
        self.add(group)

    def update_vects(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]

        self.r[0] += self.v[0]
        self.r[1] += self.v[1]
