
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from main import Main


class Game_Stats:
    def __init__(self, game: Main):
        self.settings = game.settings
        self.reset_stats()
        
    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
