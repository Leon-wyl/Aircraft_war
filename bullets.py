import pygame
from settings import Settings
from pygame.sprite import Group
from bullet import Bullet
from datetime import datetime

class Bullets(Group):

    def __init__(self):
        super(Bullets, self).__init__()
        self.firing = False
        self.loading = False
        self.last_add_time = datetime.now()
        self.aw_settings = Settings()
    
    def bullet_add(self, aw_settings, screen, ship):
        countdown = (datetime.now() - self.last_add_time).total_seconds()
        if (countdown < aw_settings.bullet_countdown):
            self.loading = True
        else:
            self.loading = False

        if self.firing == True and self.loading == False:
            new_bullet = Bullet(aw_settings, screen, ship)
            self.add(new_bullet)
            self.last_add_time = datetime.now()
            
