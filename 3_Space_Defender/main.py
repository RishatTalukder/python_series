import pygame

from alien import Alien
from settings import Settings
from ship import Ship
from bullet import Bullet


class Main():
    def __init__(self):
        # initialize pygame
        pygame.init()
        
        # initialize settings
        self.settings = Settings()
        
        # initialize the bullets
        self.bullets = pygame.sprite.Group()
        
        # initialize the aliens
        self.aliens = pygame.sprite.Group()
        
        # full screen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        # set the screen
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        ))
        
        # set the title
        pygame.display.set_caption("Space Defenders")

        # create the ship
        self.ship = Ship(self)
        self._create_alien_fleet()
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 48)
        
    def display_fps(self):

        frame_rate = str(int(self.clock.get_fps()))
        text = self.font.render(f"FPS: {frame_rate}", False, pygame.Color('white'))
        self.screen.blit(text, (0, 0))

    
    def game_loop(self):
        # main game loop
        while True:

            # check for events
            self.check_events()
            
            # update the game
            self.ship.update()
            self._update_bullets()
                    
            #update the aliens
            self._update_aliens()
            
            # update the screen
            self.update_screen()
            self.clock.tick()
            
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.display_fps()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.aliens.draw(self.screen)
        
        pygame.display.flip()
        
    def _create_alien_fleet(self):
        alien = Alien(self)
        # assert alien.rect is not None
        alien_width, alien_height = alien.rect.size
        
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        ship_height = self.ship.image_rect.height
        available_space_y = self.settings.screen_height - (4 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)
        
        print(number_aliens_x)
        
        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row)
                
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = 50 +alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)
        
    def _update_aliens(self):
        self.check_aliens_edges()
        self.aliens.update()

    def check_aliens_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._reverse_direction()
                break

    def _reverse_direction(self):
        # for alien in self.aliens.sprites():
        #     alien.rect.y += self.settings.fleet_drop_speed
        self.settings.alien_direction *= -1
            
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            
        elif event.key == pygame.K_q:
            quit()
            
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
                

if __name__ == "__main__":
    app = Main()
    app.game_loop()