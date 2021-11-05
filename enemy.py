import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, aw_settings, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.aw_settings = aw_settings
        # Load enemy picture and set it as an rect
        self.image = pygame.image.load('pictures/enemy1.png')
        self.rect = self.image.get_rect()
        # Set the rect locate on the upper left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the location
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

