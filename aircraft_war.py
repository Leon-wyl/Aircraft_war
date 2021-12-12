#!/usr/bin/python3
import sys
from typing import AsyncIterable
import pygame
from enemies import Enemies
import game_function as gf
from game_stats import GameStats
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
    stats = GameStats(aw_settings)

    bg = pygame.image.load(aw_settings.bg_image)

    # Create a ship
    ship = Ship(screen, aw_settings)
    # Create a group that stores bullets
    bullets = Bullets()
    # Create enemy
    enemies = Enemies()
    gf.create_enemies_fleet(aw_settings, screen, ship, enemies)

    while True:
        # Check what event has happened
        gf.check_events(aw_settings, screen, ship, bullets)
        if stats.game_state:
            ship.update()
            gf.update_bullets(bullets, aw_settings, screen, ship, enemies)
            gf.update_enemies(aw_settings, stats, screen, enemies, ship, bullets)
        # Update the screen
        gf.update_screen(bg, screen, ship, bullets, enemies)

run_game()