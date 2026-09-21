import pygame

from settings import Settings
from ship import Ship


class Main():
    def __init__(self):
        # initialize pygame
        pygame.init()
        
        # initialize settings
        self.settings = Settings()
        
        # set the screen
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        ))
        
        # set the title
        pygame.display.set_caption("Space Defenders")

        # create the ship
        self.ship = Ship(self)

    
    def gmae_loop(self):
        
        # main game loop
        while True:

            # check for events
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    quit()
            
            # fill the screen with the background color
            self.screen.fill(self.settings.bg_color)
            
            self.ship.blitme()

            # update the screen
            pygame.display.flip()
            

if __name__ == "__main__":
    app = Main()
    app.gmae_loop()