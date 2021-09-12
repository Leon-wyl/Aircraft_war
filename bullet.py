import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class managing the bullets fired by the ship"""

    def __init__(self, aw_settings, screen, ship):
        # Initialise bullets, the ship and the screen
        super(Bullet, self).__init__()
        self.screen = screen
        self.image_bullet = pygame.image.load(aw_settings.bullet)
        self.rect = self.image_bullet.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.speed_factor = aw_settings.bullet_speed_factor

    def update(self):
        """Move the bullet upward"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image_bullet, self.rect)



