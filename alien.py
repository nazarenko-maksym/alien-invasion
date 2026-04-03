import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen
        self.rect.x = 0 # TODO is it works?
        self.rect.y = self.rect.height

        # Store the alien's exact vertical position
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if alien at the top or bottom of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)

    def update(self):
        # TODO Move the alien up or down
        """Move the alien right or left."""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y
