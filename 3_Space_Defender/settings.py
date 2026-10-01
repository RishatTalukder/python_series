class Settings:
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 255, 171)
        
        #ship settings
        self.ship_speed = .5
        
        
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # alien settings
        self.alien_speed = 1.0
        self.alien_direction = 1
        self.alien_drop_speed = 10