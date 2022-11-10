import pygame
import time
from random import randint

pygame.init()
screen = pygame.display.set_mode((200, 200))
screen.fill((255, 255, 255))
star = pygame.image.load('../images/star.bmp')

for y in range(5):
    for x in range(5):
        screen.blit(star, (x * 38 + randint(-10, 10), y * 38 + randint(-10, 10)))

pygame.display.flip()
time.sleep(2)

#clock = pygame.time.Clock() # order?
#clock.tick(60)