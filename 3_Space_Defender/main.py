import pygame


class Main():
    def __init__(self):
        # initialize pygame
        pygame.init()
        
        # set the screen
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Space Defenders")

        # general attributes
        self.bg_color = (0,255,171)
    
    def gmae_loop(self):
        
        # main game loop
        while True:

            # check for events
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    quit()
            
            # fill the screen with the background color
            self.screen.fill(self.bg_color)

            # update the screen
            pygame.display.flip()
            

if __name__ == "__main__":
    app = Main()
    app.gmae_loop()