from __future__ import annotations
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from main import Main


class Ship:
    def __init__(self, game: Main):
        self.moving_right = False
        self.moving_left = False
        
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        self.image = pygame.image.load('resources/ship.png')
        self.image = pygame.transform.scale_by(
            self.image,
            0.2
        )
        self.image_rect = self.image.get_rect()
        
        self.image_rect.midbottom = self.screen_rect.midbottom
    
    def update(self):
        if self.moving_right:
            self.image_rect.x += 1
            
        if self.moving_left:
            self.image_rect.x -= 1
        
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)