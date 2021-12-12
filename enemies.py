import pygame
from settings import Settings
from pygame.sprite import Group
from enemy import Enemy

class Enemies(Group):
    """A class managing the groups of enemies"""

    def __init__(self):
        super(Enemies, self).__init__()
    
    def delete(self):
        for enemy in self:
            if enemy.rect.bottom <= 0:
                self.remove(enemy)
    