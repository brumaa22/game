import pygame, sys


pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_hight = 400
pygame.display.set_mode((screen_width, screen_hight))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)


