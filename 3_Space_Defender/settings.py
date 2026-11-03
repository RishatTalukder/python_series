class Settings:
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 255, 171)
        
        #ship settings
        self.ship_speed = 6
        self.ship_limit = 1
        
        
        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # alien settings
        self.alien_speed = 6.0
        self.alien_direction = 1
        self.alien_drop_speed = 10
        
        self.speed_scale = 1.1
        
        self.initialize_dynamic_settings()
        
    
    def initialize_dynamic_settings(self):
        self.ship_speed = 6
        self.bullet_speed = 10
        self.alien_speed = 6
        
        self.alien_direction = 1
        
    def increase_speed(self):
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale