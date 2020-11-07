#! python3

import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """A class dedicated to managing the resources and the way the game works."""

    def __init__(self):
        """Initializing the game and creating its resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Starting the main loop of the program."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Reaction to events generated by the keyboard and mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Updates the images on the screen and goes to a new screen."""
        # Refresh the screen during each iteration of the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Waiting for a key or mouse button to be pressed.
        pygame.display.flip()

if __name__ == '__main__':
    #Creation of a copy of the game and its launch.
    ai = AlienInvasion()
    ai.run_game()
