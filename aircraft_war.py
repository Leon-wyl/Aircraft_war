#!/usr/bin/python3
import sys
import pygame
import game_function as gf
from settings import Settings
from ship import Ship
from bullets import Bullets

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

    while True:
        # Check what event has happened
        gf.check_events(aw_settings, screen, ship, bullets)

        # Update the state of the ship and bullets according to the event
        ship.update()
        bullets.bullet_add(aw_settings, screen, ship)
        bullets.update()

        # Update the screen
        gf.update_screen(bg, screen, ship, bullets)

run_game()