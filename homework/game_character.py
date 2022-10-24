import pygame
import time


class Zombie:
    """Lets create the zombie!!"""
    def __init__(self, screen):
        self.image = pygame.image.load('../images/character_zombie_attack0.bmp')
        self.rect = self.image.get_rect()
        self.screen = screen
        screen_rect = screen.get_rect()
        self.rect.center = screen_rect.center

    def draw(self):
        """Draw self"""
        self.screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((200, 200))
screen.fill((128, 255, 255))
zombie = Zombie(screen)
zombie.draw()
pygame.display.flip()
time.sleep(4)
