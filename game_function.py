import sys
import pygame
from bullet import Bullet

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


def update_screen(bg, screen, ship, bullets):
    screen.blit(bg,(0,0))
    for bullet in bullets.sprites():
        bullet.blitme()
    ship.blitme()
    pygame.display.flip()

def bullet_delete(bullets):
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)