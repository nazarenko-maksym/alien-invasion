import sys

import pygame
from random import randint

from settings import Settings
from raindrop import Raindrop


FPS = 60
FULLSCREEN_MODE = False

class Rain:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        if FULLSCREEN_MODE:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )

        pygame.display.set_caption("Rain")

        self.raindrops = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(FPS)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _update_raindrops(self):
        """Check if the raindrop is in the bottom, then update positions."""
        self._check_rain_bottom_edge()
        self.raindrops.update()

    def _create_rain(self):
        """Create the rain."""
        # Create a raindrop and keep adding raindrops untill there's no room left
        # Spacing between raindrops is one raindrop width and one raindrop height
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.settings.screen_height - 2 * raindrop_height):
            while current_x < (self.settings.screen_width - 2 * raindrop_width):
                if randint(0,1):
                    self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width
            # Finished a row; reset x value, and increment y value
            current_x = raindrop_width
            current_y += 2 * raindrop_height

    def _create_rain_line(self, raindrop_width, raindrop_height):
        """Create one horizontal line of raindrops."""
        current_x, current_y = raindrop_width, raindrop_height
        while current_x < (self.settings.screen_width - 2 * raindrop_width):
            if randint(0,1):
                self._create_raindrop(current_x, current_y)
            current_x += 2 * raindrop_width

    def _create_raindrop(self, x_position, y_position):
        """Create a raindrop and place it in the rain."""
        new_raindrop = Raindrop(self)
        new_raindrop.x = x_position
        new_raindrop.y = y_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)

    def _check_rain_bottom_edge(self):
        """Respond appropriately if any raindrop have reached bottom."""
        for raindrop in self.raindrops.copy():
            if raindrop.check_bottom_edge():
                self._remove_raindrops(raindrop)
                raindrop_width, raindrop_height = raindrop.rect.size
                self._create_rain_line(raindrop_width, raindrop_height)
                break
        print(len(self.raindrops))

    def _remove_raindrops(self, raindrop):
        """Remove the raindrop from bottom of the screen."""
        for raindrop in self.raindrops.copy():
            if raindrop.check_bottom_edge():
                self.raindrops.remove(raindrop)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    rain = Rain()
    rain.run_game()
