import pygame
import ships.ship
import ships.shiplayer
import player
import util


class Kasada():
    player = None
    ship = None

    screen = None
    to_draw = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.player = player.Player(self)
        self.ship = ships.ship.Ship(self)
        self.to_draw = pygame.sprite.RenderUpdates()

    def run(self):
        pygame.display.flip()
        print("test")