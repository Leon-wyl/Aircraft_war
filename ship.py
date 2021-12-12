import pygame

class Ship():

    def __init__(self, screen, aw_settings):
        # Initialise the ship and the screen
        self.screen = screen
        self.aw_settings = aw_settings
        self.image_ship = pygame.image.load(aw_settings.aircraft)
        self.rect = self.image_ship.get_rect()
        self.screen_rect = screen.get_rect()

        self.position_init()
        
        # Moving marks
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image_ship, self.rect)
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.aw_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.aw_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.centery -= self.aw_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.aw_settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def position_init(self):
        """Initialize the position of the ship"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
    