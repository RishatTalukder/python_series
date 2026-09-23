from __future__ import annotations
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from main import Main


class Ship:
    def __init__(self, game: Main):
        
        self.moving_right = False
        self.moving_left = False
        
        # get the game object
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        self.image = pygame.image.load('resources/ship.png')
        self.image = pygame.transform.scale_by(
            self.image,
            0.2
        )
        self.image_rect = self.image.get_rect()
        self.image_rect.midbottom = self.screen_rect.midbottom
        
        self.x = float(self.image_rect.x)
        
    def update(self):
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            
        if self.moving_left and self.image_rect.left > 0:
            self.x -= self.settings.ship_speed
            
        self.image_rect.x = self.x
        
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)