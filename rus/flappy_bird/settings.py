class Settings():
    """Содержит все настройки игры Flappy Bird."""

    def __init__(self):
        # Настройки экрана.
        self.screen_width = 1920
        self.screen_height = 1070
        self.screen_color = (255, 255, 255)
        # Настройки птицы.
        self.jump_height = 100
        self.bird_falling_speed = 2
        self.bird_lives = 3
        # Настройки стен.
        self.walls_speed = 3
        self.distance_between_walls = (250, 600)  # id 0 - расстояние между верхней и нижней стеной,
        # id 1 - расстояние от одной пары стен до другой.
