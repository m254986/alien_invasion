import pygame
import time

class Star:
    def __init__(self, screen):
        self.image = pygame.image.load('../images/star.bmp')
        self.rect = self.image.get_rect()
        self.screen = screen
        screen_rect = screen.get_rect()
        self.rect.center = screen_rect.center

    def draw(self):
        """Draw self"""
        self.screen.blit(self.image, self.rect)

class Fleet:


pygame.init()
screen = pygame.display.set_mode((200, 200))
screen.fill((255, 255, 255))
star = Star(screen)
star.draw()
pygame.display.flip()
time.sleep(4)

#clock = pygame.time.Clock() # order?
#clock.tick(60)