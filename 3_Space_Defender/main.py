import pygame


class Main():
    def __init__(self):
        pygame.init()
        
        # the screen
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Space Defenders")
        
    
    def gmae_loop(self):
        
        while True:
            
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    quit()
                    
                    
            pygame.display.flip()
            

if __name__ == "__main__":
    app = Main()
    app.gmae_loop()