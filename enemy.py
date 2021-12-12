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
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.aw_settings.enemy_speed_factor
        self.rect.y = self.y

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        

