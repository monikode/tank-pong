

from logging.config import listen
import pygame
from config import SCREEN_RECTS, TANK_1_COLOR, TANK_2_COLOR
from screen import Screen
from tank import Tank


class Game:
    def __init__(self) -> None:

        self.playing = True
        self.screen = Screen()
        self.score = (0, 0)
        self.font = pygame.font.Font("img/DSEG14Classic-Bold.ttf", 34)
        self.score_p1 = self.font.render(str(self.score[0]), True, TANK_1_COLOR)
        self.score_p2 = self.font.render(str(self.score[1]), True, TANK_2_COLOR)
        self.clock = pygame.time.Clock()
        self.map = SCREEN_RECTS
        self.tank1 = Tank((45, 243), TANK_1_COLOR, pygame.K_LEFT,
                          pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN)
        self.tank2 = Tank((710, 243), TANK_2_COLOR, pygame.K_a,
                          pygame.K_w, pygame.K_d, pygame.K_s)
        # TODO declarar as classes (Tank, Ball, etc aqui)

    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def listen_keyboard(self):
        self.tank1.move(
            self.map + [(self.tank2.x, self.tank2.y, self.tank2.size, self.tank2.size)])
        self.tank2.move(
            self.map + [(self.tank1.x, self.tank1.y, self.tank1.size, self.tank1.size)])
        # TODO chamar funções de movimentação do tanque aqui

    def loop(self):
        while self.playing:
            # TODO chamar funcao de movimentacao dda bola aqui (ex: Ball.move(self.map))
            self.listen_events()
            self.listen_keyboard()
            # funcao draw recebe as coordenadas e a rotacao, no caso no tanque
            self.screen.draw(self.map, [(0, 0), 0], [(0, 0), 0], (0, 0))
            self.screen.arena.blit(
                self.tank1.get_image(), (self.tank1.x, self.tank1.y))
            self.screen.arena.blit(
                self.tank2.get_image(), (self.tank2.x, self.tank2.y))

            #  Score HUD
            self.screen.surface.blit(self.score_p1, (220, 20))
            self.screen.surface.blit(self.score_p2, (550, 20))

            pygame.display.flip()
            self.clock.tick(60)
