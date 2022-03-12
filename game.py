

from logging.config import listen
import pygame
from screen import Screen


class Game:
    def __init__(self) -> None:

        self.playing = True
        self.screen = Screen()

    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def listen_keyboard (self):
        pass

    def loop(self):
        while self.playing:
            self.listen_events()
            self.listen_keyboard()
            self.screen.draw(0, 0, 0)
            pygame.display.flip()
