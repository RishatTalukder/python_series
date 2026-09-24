import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Main

class Bullet(Sprite):
    
    def __init__(self, game: Main):
        
        super().__init__()
        
        # get the game
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        
        # make the bullet
        self.rect : pygame.Rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.image_rect.midtop
        
        # get the bullet position
        self.y = float(self.rect.y)
        
        
    def update(self):
        # update the bullet
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)