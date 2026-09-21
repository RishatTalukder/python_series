from __future__ import annotations
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from main import Main


class Ship:
    def __init__(self, game: Main):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        self.image = pygame.image.load('resources/ship.png')
        self.image_rect = self.image.get_rect()
        
        self.image_rect.midbottom = self.screen_rect.midbottom
        
        
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)