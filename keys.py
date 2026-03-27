import sys

import pygame

from settings import Settings


FPS = 10
BLACK = (0, 0, 0)

class Keys:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.font = pygame.font.Font(None, 100)

        self.last_key_pressed = ""

        pygame.display.set_caption("Keys")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
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
        if event.key >= 0 and event.key <= 256:
            self.last_key_pressed = event.unicode
            print(f"{event.unicode} - {event.key}")

    def _draw_text(self, text, color):
        textobj = self.font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = self.screen.get_rect().center
        self.screen.blit(textobj, textrect)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self._draw_text(self.last_key_pressed, BLACK)

        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    keys = Keys()
    keys.run_game()
