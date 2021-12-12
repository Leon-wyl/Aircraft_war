import sys
import pygame
from bullet import Bullet
from enemy import Enemy
from random import randint

def check_keydown_event(event, aw_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        bullets.firing = True
        bullets.loading = True
    elif event.key == pygame.K_SPACE:
        sys.exit()

def check_keyup_event(event, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_SPACE:
        bullets.firing = False

def check_events(aw_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, aw_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship, bullets)


def update_screen(bg, screen, ship, bullets, enemies):
    screen.blit(bg,(0,0))
    for bullet in bullets.sprites():
        bullet.blitme()
    ship.blitme()
    enemies.draw(screen)
    pygame.display.flip()

def bullet_delete(bullets):
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_bullets(bullets, aw_settings, screen, ship, enemies):
    bullets.bullet_add(aw_settings, screen, ship)
    bullets.update()
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if len(enemies) == 0:
        bullets.empty()
        create_enemies_fleet(aw_settings, screen, ship, enemies)
    bullets.bullet_delete()

def create_enemies_fleet(aw_settings, screen, ship, enemies):
    """Create a group of enemies"""
    # create an enemy, calculate how many enemies a line can have
    # distance between enemies are twice the width of enemy
    enemy = Enemy(aw_settings, screen)
    enemy_width = enemy.rect.width
    num_enemy_per_line = get_number_enemies_per_line(aw_settings, enemy_width)
    num_rows = get_number_rows(aw_settings, ship.rect.height, enemy.rect.height)

    # Create lines of enemy
    for row_number in range(num_rows):
        for enemy_number in range(num_enemy_per_line):
            random_number = randint(0, num_enemy_per_line)
            if (random_number > num_enemy_per_line / 1.5):
                create_enemy(aw_settings, screen, enemies, enemy_number, row_number)
                print("created")

def get_number_enemies_per_line(aw_settings, enemy_width):
    available_space_per_line = aw_settings.screen_width - 1.5 * enemy_width
    num_enemy_per_line = int(available_space_per_line / (1.5 * enemy_width)) - 1
    return num_enemy_per_line

def get_number_rows(aw_settings, ship_height, enemy_height):
    """Calculate how many lines of enemies can be shown on the screen"""
    available_space_height = (aw_settings.screen_height - 3 * enemy_height - ship_height)
    num_rows = int(available_space_height / (2 * enemy_height))
    return num_rows


def create_enemy(aw_settings, screen, enemies, enemy_number, row_number):
    enemy = Enemy(aw_settings, screen)
    enemy_width = enemy.rect.width
    enemy.x = 0.5 * enemy_width + 2 * enemy_width * enemy_number
    enemy.rect.x = enemy.x
    enemy.y = enemy.rect.height + 2 * enemy.rect.height * row_number
    enemy.rect.y = enemy.y
    enemies.add(enemy)

def update_enemies(enemies):
    enemies.update()
    enemies.delete()
