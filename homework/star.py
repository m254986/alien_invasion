import pygame
import time

pygame.init()
screen = pygame.display.set_mode((200, 200))
screen.fill((255, 255, 255))
star = pygame.image.load('../images/star.bmp')

for y in range(5):
    for x in range(5):
        screen.blit(star, (x * 38, y * 38))

pygame.display.flip()
time.sleep(4)

#clock = pygame.time.Clock() # order?
#clock.tick(60)