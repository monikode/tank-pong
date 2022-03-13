

from logging.config import listen
from sqlite3 import Time
from time import time
import pygame
from bullet import Bullet
from config import SCREEN_RECTS, TANK_1_COLOR, TANK_2_COLOR
from screen import Screen
from tank import Tank


class Game:
    def __init__(self) -> None:

        self.playing = True
        self.screen = Screen()
        self.score = (0, 0)
        self.font = pygame.font.Font("img/DSEG14Classic-Bold.ttf", 34)
        self.score_p1 = self.font.render(
            str(self.score[0]), True, TANK_1_COLOR)
        self.score_p2 = self.font.render(
            str(self.score[1]), True, TANK_2_COLOR)
        self.clock = pygame.time.Clock()
        self.map = SCREEN_RECTS
        self.tank1 = Tank((45, 243), TANK_1_COLOR, pygame.K_LEFT,
                          pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_SPACE)
        self.tank2 = Tank((710, 243), TANK_2_COLOR, pygame.K_a,
                          pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_q)

    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def listen_keyboard(self):
        self.tank1.move(
            self.map + [self.tank2.get_rect()])
        self.tank2.move(
            self.map + [self.tank1.get_rect()])

    def loop(self):
        while self.playing:
            self.listen_events()
            self.listen_keyboard()

            self.screen.draw(self.map, [(0, 0), 0], [(0, 0), 0], (0, 0))
            self.tank1.draw(self.screen.arena)
            self.tank2.draw(self.screen.arena)

            #  Score HUD
            self.screen.surface.blit(self.score_p1, (220, 20))
            self.screen.surface.blit(self.score_p2, (550, 20))

            pygame.display.flip()
            self.clock.tick(60)
