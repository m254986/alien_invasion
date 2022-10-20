import pygame
import time

pygame.init()
screen = pygame.display.set_mode((200, 200))
screen.fill((128, 255, 255))

zombie = pygame.image.load('../images/character_zombie_attack0.bmp')

zombie_rect = zombie.get_rect()
screen_rect = screen.get_rect()
zombie_rect.center = screen_rect.center # move to center

#draw or blit the zombie onto screen!
screen.blit(zombie, zombie_rect)

class Zombie:
    """Lets create the zombie!!"""
    def __init__(self, screen):
        self.rect = Zombie.get_rect()
        self.image = pygame.image.load('../images/character_zombie_attack0.bmp')
        self.screen = screen

    def blitme(self):
        """Draw self"""
        self.screen.blit(self.image, self.rect)

pygame.display.flip()
time.sleep(4)