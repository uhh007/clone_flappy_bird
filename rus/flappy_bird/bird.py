import pygame


class Bird():
    def __init__(self, screen, settings):
        """Инициализирует настройки птицы."""
        self.screen = screen
        self.settings = settings

        # Загружаем изображение и задаём ему рамку.
        self.image = pygame.image.load(r'.\img\models\bird\frame-1.png')
        self.rect = self.image.get_rect()

        # Задаём начальное положение птицы.
        self.rect.bottom = self.settings.screen_height
        self.rect.left = 150

        # Создаём флаг прыжка.
        self.jump = False

    def anim1(self):
        """Обновляет фото птицы, тем самым создавая анимацию.(1)"""
        self.image = pygame.image.load(r'.\img\models\bird\frame-2.jpg')

    def anim2(self):
        """Обновляет фото птицы, тем самым создавая анимацию.(2)"""
        self.image = pygame.image.load(r'.\img\models\bird\frame-1.png')

    def start_pos(self):
        """Ставит птицу в начальное положение."""
        self.rect.bottom = self.settings.screen_height
        self.rect.left = 150

    def update(self):
        """Опускает птицу."""
        if self.rect.bottom != self.settings.screen_height:
            self.rect.y += self.settings.bird_falling_speed

    def blit_me(self):
        """Рисует птицу на экране."""
        self.screen.blit(self.image, self.rect)