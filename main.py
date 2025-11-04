import pygame
from input import Input

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.input = Input(self)

        while self.running:
            self.input.eventHandler()
            self.screen.fill("white")
            pygame.display.flip()

            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()