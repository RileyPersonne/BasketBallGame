import pygame
from player import Player


class Input:
    def __init__(self, parent):
        self.player = Player()
        self.parent = parent

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.parent.running = False