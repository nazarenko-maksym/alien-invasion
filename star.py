import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star in the sky."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load the image of star and set its rect attribute
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # Set each new star near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store hotizantal position of the star
        self.x = float(self.rect.x)
