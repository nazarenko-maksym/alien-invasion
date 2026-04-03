import pygame


class Ship:
    """A class to manage ship."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.game_direction = game.game_direction

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Set settings dependable on the game
        if self.game_direction == 'horizontal':
            # Start each new ship at the bottom center of the screen.
            self.rect.midbottom = self.screen_rect.midbottom
        elif self.game_direction == 'vertical':
            # Rotate the image of the shit by 90 degrees clockwise
            self.image = pygame.transform.rotate(self.image, -90)
            # Start each new ship at the left center of the screen.
            self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact vertical position.
        self.y = float(self.rect.y)
        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship_midleft(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Update rect object from self.x or self.y
        self.rect.y = self.y
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
