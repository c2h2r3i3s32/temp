import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Enemies")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 40, 40)  
player_speed = 5

enemies = []
enemy_speed = 3
enemy_spawn_timer = 0
enemy_spawn_interval = 60 

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed
    
    enemy_spawn_timer += 1
    if enemy_spawn_timer >= enemy_spawn_interval:
        enemy_rect = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)  # x, y, width, height
        enemies.append(enemy_rect)
        enemy_spawn_timer = 0
    
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
    
    pygame.draw.rect(screen, RED, player_rect)
    
    for enemy in enemies:
        pygame.draw.rect(screen, BLUE, enemy)
    
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            print("Game Over!")
            running = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

