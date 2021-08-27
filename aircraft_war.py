#!/usr/bin/python3
import sys
import pygame
import game_function as gf
from settings import Settings
from ship import Ship

def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    aw_settings = Settings()
    screen = pygame.display.set_mode((aw_settings.screen_width, aw_settings.screen_height))
    pygame.display.set_caption("Aircraft War")

    bg = pygame.image.load(aw_settings.bg_image)

    # Create a ship
    ship = Ship(screen, aw_settings)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(bg, screen, ship)


run_game()