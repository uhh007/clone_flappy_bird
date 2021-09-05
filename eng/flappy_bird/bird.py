import pygame


class Bird():
    def __init__(self, screen, settings):
        """Initialize bird settings."""
        self.screen = screen
        self.settings = settings

        # Load the image and give it a frame.
        self.image = pygame.image.load(r'.\img\models\bird\frame-1.png')
        self.rect = self.image.get_rect()

        # We set the initial position of the bird.
        self.rect.bottom = self.settings.screen_height
        self.rect.left = 150

        # Create a jump flag.
        self.jump = False

    def anim1(self):
        """Update the bird photo, thus creating an animation. (1)"""
        self.image = pygame.image.load(r'.\img\models\bird\frame-2.jpg')

    def anim2(self):
        """Update the bird photo, thus creating an animation. (2)"""
        self.image = pygame.image.load(r'.\img\models\bird\frame-1.png')

    def start_pos(self):
        """Puts the bird in the starting position."""
        self.rect.bottom = self.settings.screen_height
        self.rect.left = 150

    def update(self):
        """Drops a bird."""
        if self.rect.bottom != self.settings.screen_height:
            self.rect.y += self.settings.bird_falling_speed

    def blit_me(self):
        """Draws a bird on the screen."""
        self.screen.blit(self.image, self.rect)