import pygame
from pygame.sprite import Sprite


class Carrot(Sprite):
    def __init__(self, settings):
        """Initialize the carrot."""
        Sprite.__init__(self)

        self.settings = settings
        # Load the image and set the frame.
        self.image = pygame.image.load('./img/models/carrot/carrot.png')
        self.rect = self.image.get_rect()

    def update(self):
        """Update the position of the carrot on the screen."""
        self.rect.x -= self.settings.walls_speed