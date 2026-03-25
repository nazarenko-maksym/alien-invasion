import pygame


class Penguin:
    """A class to manage character."""

    def __init__(self, ai_screen):
        self.screen = ai_screen.screen
        self.screen_rect = self.screen.get_rect()

        # Load the penguin image and get its rect
        self.image = pygame.image.load('images/penguin.bmp')
        self.rect = self.image.get_rect()

        # Start each new penguin in the center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the penguin to its current location."""
        self.screen.blit(self.image, self.rect)
