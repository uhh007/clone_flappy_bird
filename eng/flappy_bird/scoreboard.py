import pygame.font
from pygame.sprite import Group
from bird import Bird


class Scoreboard():
    """Class for displaying game information."""
    def __init__(self, settings, screen, stats):
        """Initializes the scoring attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings for image output.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Preparing the original image.
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Converts the current account to a graphical display."""
        score = self.stats.score
        score_str = 'Caught carrots: ' + "{:,}".format(score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.screen_color)

        # Account withdrawal in the upper right part of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Converts the current account to a graphical display."""
        high_score = self.stats.high_score
        high_score_str = 'Record: ' + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                self.settings.screen_color)

        # Account withdrawal in the upper right part of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 80

    def show_score(self):
        """Displays the current score, record and the number of remaining ships on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)