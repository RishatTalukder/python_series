
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from main import Main


class Game_Stats:
    def __init__(self, game: Main):
        self.game_active = False
        self.settings = game.settings
        self.high_score = 0
        self.reset_stats()
        
    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1