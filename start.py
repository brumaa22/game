import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("runner")
clock = pygame.time.Clock()
test_surface = pygame.transform.scale(pygame.image.load("graphics/pixil-frame-0.png"),(800, 700)).convert_alpha()
enemy = pygame.transform.scale(pygame.image.load("graphics/pixil-frame-0 (8).png"),(45, 70)).convert_alpha()
ground = pygame.transform.scale(pygame.image.load("graphics/pixil-frame-0 (9).png"),(752, 72)).convert_alpha()
player = pygame.transform.scale(pygame.image.load("graphics/pixil-frame-0 (7).png"),(45, 70)).convert_alpha()
player_box = player.get_rect(topleft = (50, 270))
enemy_rect = enemy.get_rect(topleft = (700, 290))
ground_rect = ground.get_rect(topleft = (24, 360))
player_gravity = 0
def movement():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            player_box.x = 1




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -15
        movement()


    if player_box.bottom >= 360: player_box.bottom = 360
        #if player_box.colliderect(ground_rect):
         #   player_gravity -1

        #mouse pos test
        #if event.type == pygame.MOUSEMOTION:
         #   print(event.pos)



    screen.blit(test_surface,(0, 0))
    screen.blit(enemy, enemy_rect)
    screen.blit(ground, (24, 360))
    screen.blit(player, player_box)

    player_box.y += player_gravity
    player_gravity += 1


    enemy_rect.x -= 4
    if enemy_rect.x <= -40:
        enemy_rect.x = 820


    pygame.display.update()
    clock.tick(60)