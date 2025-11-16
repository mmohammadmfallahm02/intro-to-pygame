import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()
score_suf = test_font.render('My game', False, 'Black')
score_rect = score_suf.get_rect(center = (400,50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect =snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

player_gravity = 0

while True:
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
             
                # print("Jump")
                
                player_gravity = -20

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen,'pink',score_rect)
    pygame.draw.rect(screen,'pink',score_rect,10)
    screen.blit(score_suf, score_rect)
    
    
    snail_rect.left -= 5
    if snail_rect.left < -50: snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    
    player_gravity += 1
    player_rect.y += player_gravity
    if(player_rect.bottom >= 300):
        player_rect.bottom = 300
    
    screen.blit(player_surf, player_rect)
    
    
    if snail_rect.colliderect(player_rect):
        pygame.quit()
        exit()
    

    pygame.display.update()
    clock.tick(60)