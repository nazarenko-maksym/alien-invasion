import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.game_direction = game.game_direction

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        # Store the alien's exact vertical position
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def check_vertical_edges(self):
        """Return true if alien at the top or bottom of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)

    def update_vertical(self):
        """Move the alien up or down."""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y

    def update(self):
        """Move the alien right or left."""
        if self.game_direction == 'horizontal':
            self.x += self.settings.alien_speed * self.settings.fleet_direction
            self.rect.x = self.x
        elif self.game_direction == 'vertical':
            self.y += self.settings.alien_speed * self.settings.fleet_direction
            self.rect.y = self.y
