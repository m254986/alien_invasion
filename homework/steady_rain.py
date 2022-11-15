import pygame
from pygame.sprite import Sprite
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
raindrop = pygame.image.load('../images/raindrop.bmp')
raindrop_rect = raindrop.get_rect()
screen_rect = screen.get_rect()

TILE_SIZE_X = 74*1.25
TILE_SIZE_Y = 100*1.25
num_tiles = screen_rect.width // raindrop_rect.width
y_offset = raindrop_rect.y
clock = pygame.time.Clock()

class Raindrop(Sprite):
    def __init__(self):
        screen.fill((255, 255, 255))
        for y in range(num_tiles):
            for x in range(num_tiles):
                y_coordinate = y*TILE_SIZE_Y + y_offset
                screen.blit(raindrop, (x * TILE_SIZE_X, y_coordinate))

        y_offset = y_offset + 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

    def _check_events(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

        y += y_offset
        self.rect.y = self.y