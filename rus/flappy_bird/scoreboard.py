import pygame.font
from pygame.sprite import Group
from bird import Bird


class Scoreboard():
    """Класс для вывода игровой информации."""
    def __init__(self, settings, screen, stats):
        """Инициализирует атрибуты подсчёта очков."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Настройки шрифта для вывода изображения.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка исходного изображения.
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Преобразует текущий счёт в графическое изображение."""
        score = self.stats.score
        score_str = 'Поймано морковок: ' + "{:,}".format(score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.screen_color)

        # Вывод счёта в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Преобразует текущий счёт в графическое изображение."""
        high_score = self.stats.high_score
        high_score_str = 'Рекорд: ' + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                self.settings.screen_color)

        # Вывод счёта в правой верхней части экрана.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 80

    def show_score(self):
        """Выводит текущий счёт, рекорд и число оставшихся кораблей на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)