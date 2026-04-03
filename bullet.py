import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.game_direction = game.game_direction

        # Create a bullet rect at (0, 0) and then set correct position
        if self.game_direction == 'horizontal':
            self.rect = pygame.Rect(
                0, 0,
                self.settings.bullet_width, self.settings.bullet_height
            )
            self.rect.midtop = game.ship.rect.midtop
        elif self.game_direction == 'vertical':
            self.rect = pygame.Rect(
                0, 0,
                self.settings.bullet_vertical_width,
                self.settings.bullet_vertical_height
            )
            self.rect.midright = game.ship.rect.midright

        # Store the bullet's position as a float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        if self.game_direction == 'horizontal':
            # Update the exact position of the bullet
            self.y -= self.settings.bullet_speed
            # Update the rect position
            self.rect.y = self.y
        elif self.game_direction == 'vertical':
            # Update the exact position of the bullet
            self.x += self.settings.bullet_speed
            # Update the rect position
            self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
