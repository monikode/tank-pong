

from logging.config import listen
import pygame
from config import SCREEN_RECTS
from screen import Screen


class Game:
    def __init__(self) -> None:

        self.playing = True
        self.screen = Screen()
        self.score = (0, 0)
        self.map = SCREEN_RECTS
        # TODO declarar as classes (Tank, Ball, etc aqui)

    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def listen_keyboard (self):
        # TODO chamar funções de movimentação do tanque aqui
        pass

    def loop(self):
        while self.playing:
            #TODO chamar funcao de movimentacao dda bola aqui (ex: Ball.move(self.map))
            self.listen_events()
            self.listen_keyboard()
            self.screen.draw(self.map, 0, 0, 0)
            pygame.display.flip()
