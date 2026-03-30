import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """A class to represent a single rain droplet in the rain."""

    def __init__(self, rain_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = rain_game.screen
        self.settings = rain_game.settings

        # Load the image and set its rect attribute
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new droplet near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the exact raindrop horizontal and vertical positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_bottom_edge(self):
        """Return true if raindrop is in the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom)

    def update(self):
        """Move the raindrop down."""
        self.y += self.settings.raindrop_drop_speed
        self.rect.y = self.y
