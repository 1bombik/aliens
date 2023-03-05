class Settings:
    """Game settings"""

    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (20, 20, 30)
        self.ship_speed = 1.5

        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (200, 10, 200)
        self.bullets_allowed = 999999999
