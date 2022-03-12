import pygame

from config import BG_COLOR, RECTS_COLOR, SCREEN_HEIGHT, SCREEN_RECTS, SCREEN_WIDTH, TOP_BAR_HEIGHT


class Screen:
    surface: pygame.Surface

    def __init__(self) -> None:
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.arena = self.surface.subsurface(
            (0, TOP_BAR_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - TOP_BAR_HEIGHT))

    def draw(self, map, tank1, tank2, balls):
        self.surface.fill(BG_COLOR)

        for rect in map:
            pygame.draw.rect(self.arena, RECTS_COLOR, rect)
