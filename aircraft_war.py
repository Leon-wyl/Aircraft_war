#!/usr/bin/python3
import sys
import pygame
from enemies import Enemies
import game_function as gf
from settings import Settings
from ship import Ship
from bullets import Bullets
from enemies import Enemies

def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    aw_settings = Settings()
    screen = pygame.display.set_mode((aw_settings.screen_width, aw_settings.screen_height))
    pygame.display.set_caption("Aircraft War")

    bg = pygame.image.load(aw_settings.bg_image)

    # Create a ship
    ship = Ship(screen, aw_settings)
    # Create a group that stores bullets
    bullets = Bullets()
    # Create enemy
    enemies = Enemies()
    gf.create_enemies_fleet(aw_settings, screen, ship, enemies)
    for enemy in enemies:
        print(enemy.rect.y)
    gf.update_enemies(enemies)
    for enemy in enemies:
        print(enemy.rect.y)

    while True:
        # Check what event has happened
        gf.check_events(aw_settings, screen, ship, bullets)

        # Update the state of the ship and bullets according to the event
        ship.update()

        gf.update_bullets(bullets, aw_settings, screen, ship, enemies)

        # Update positions of the enemies
        gf.update_enemies(enemies)

        # Update the screen
        gf.update_screen(bg, screen, ship, bullets, enemies)

run_game()