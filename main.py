import pygame
import ships.ship
import ships.shiplayer
import player


class Kasada():
    player = None
    ship = None

    screen = None
    to_draw = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 650))
        self.run()

    def run(self):
        done = False

        self.to_draw = pygame.sprite.RenderUpdates()
        self.player = player.Player(self, self.to_draw)
        self.ship = ships.ship.Ship(self)

        clock = pygame.time.Clock()

        while not done:
            self.screen.fill((0, 0, 0))
            self.ship.draw(self.screen)
            self.to_draw.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            if pygame.sprite.collide_mask(self.ship.outer, self.player):
                self.ship.outer.visible = 0
                self.player.a[1] = 1
            else:
                self.ship.outer.visible = 1
                self.player.a[1] = 0
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: self.player.v[1] -= 1
            if pressed[pygame.K_DOWN]: self.player.v[1] += 1
            if pressed[pygame.K_LEFT]: self.player.v[0] -= 1
            if pressed[pygame.K_RIGHT]: self.player.v[0] += 1
            self.player.update_vects()
            if self.player.ship_collide(self.ship):
                self.player.a[0] = 0
                self.player.a[1] = 0
                self.player.v[0] = 0
                self.player.v[1] = 0
            self.ship.set_rect()

            pygame.display.flip()
            clock.tick(60)


test = Kasada()
