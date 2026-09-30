from typing import TYPE_CHECKING

import pygame 
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from main import Main

class Alien(Sprite):
    
    def __init__(self, game: Main):
        super().__init__()
        
        self.screen = game.screen
        self.settings = game.settings
        
        self.image = pygame.image.load('resources/alien.svg')
        self.image = pygame.transform.scale_by(
            self.image,
            0.1
        )
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
        print(f'alien initial position: {self.rect.x}, {self.rect.y}')
        
    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed*self.settings.alien_direction)
        self.rect.x = self.x