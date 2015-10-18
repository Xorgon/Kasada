import pygame

class Test():

    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((1000, 650))
        self.run()

    def run(self):
        done = False

        while not done:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True

                pygame.display.flip()

Test()