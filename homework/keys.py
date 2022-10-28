import pygame

pygame.init()
screen = pygame.display.set_mode((200, 200))
screen.fill((128, 255, 255))
pygame.display.flip()

while True:
    # step 1 check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # keydown, also no self!!
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Key has been pressed!")
            elif event.key == pygame.K_q:
                sys.exit()
        # keyup
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                print("Key has been pressed!")