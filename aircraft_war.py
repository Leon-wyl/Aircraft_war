#!/usr/bin/python3
import sys
import pygame
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
    ship = Ship(screen)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(bg,(0,0))
        ship.blitme()
        pygame.display.flip()

run_game()