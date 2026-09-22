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
            self.check_events()
            # update the screen
            self.update_screen()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.image_rect.x += 10
                
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    app = Main()
    app.gmae_loop()