from typing import TYPE_CHECKING

import pygame 
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from main import Main

class Alien(Sprite):
    
    def __init__(self, game: Main):
        super().__init__()
        
        self.screen = game.screen
        
        self.image = pygame.image.load('resources/alien.svg')
        self.image = pygame.transform.scale_by(
            self.image,
            0.2
        )
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
        print(f'alien initial position: {self.rect.x}, {self.rect.y}')
        
        