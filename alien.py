import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A Class to rep a single alien in da fleet."""

    def __init__(self, ai_game):
        """Init alien and start pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load img and set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store horiz pos
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right!"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x