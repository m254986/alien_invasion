import pygame
import time

class Rocket:
    """Lets build a rocket!!"""
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Display our rocket!!"""
        self.screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((200, 200))
rocket = Rocket(screen)

while True:
    # step 1 check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # keydown, also no self!!
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
            # different!! adding up and down arrows!!
            elif event.key == pygame.K_UP:
                rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True
            elif event.key == pygame.K_q:
                sys.exit()
        # keyup
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_UP:
                rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False

    # ship updates!!
    if

screen.fill((128, 255, 255))

rocket.blitme()
pygame.display.flip()
time.sleep(4)