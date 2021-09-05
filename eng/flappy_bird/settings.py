class Settings():
    """Contains all the settings for the Flappy Bird."""

    def __init__(self):
        # Screen settings.
        self.screen_width = 1920
        self.screen_height = 1070
        self.screen_color = (255, 255, 255)
        # Bird settings.
        self.jump_height = 100
        self.bird_falling_speed = 2
        self.bird_lives = 3
        # Walls settings.
        self.walls_speed = 3
        self.distance_between_walls = (250, 600)  # id 0 - distance between top and bottom wall,
        # id 1 - distance from one pair of walls to another.
