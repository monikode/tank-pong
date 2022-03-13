from random import random
import pygame
from bullet import Bullet

from config import SPEED


class Tank:
    size = 45

    def __init__(self, initial_coord,  color, key_left, key_up, key_right, key_down, key_shoot):
        self.tank_sprite = pygame.image.load(
            "img/tank.png")
        self.tank_sprite.fill(color, None, pygame.BLEND_MAX)
        self.color = color
        self.tank_angle = 0
        self.x = initial_coord[0]
        self.y = initial_coord[1]
        self.direction = 1
        self.x_velocity = 0
        self.y_velocity = 0
        self.angle = 0

        self.key_up = key_up
        self.key_down = key_down
        self.key_right = key_right
        self.key_left = key_left
        self.key_shoot = key_shoot

        self.bullets = []
        self.shooted = False
        self.spin = False
        self.start_spin = 0

    def listen_keyboard(self):
        key = pygame.key.get_pressed()
        if key[self.key_left]:
            self.angle -= 1
        if key[self.key_down]:
            self.direction = 1
        if key[self.key_right]:
            self.angle += 1
        if key[self.key_up]:
            self.direction = -1
        if key[self.key_shoot]:
            if not self.shooted:
                self.bullets.append(
                    Bullet(self.x + self.size/2, self.y + self.size/2,-self.x_velocity / SPEED, -self.y_velocity/SPEED))
            self.shooted = True
        else:
            self.shooted = False

    def move(self, map):
        self.direction = 0
        self.listen_keyboard()

        quad = self.angle/90  # ver se ta pra direita esquerda etc
        deg = quad % 1  # ver se ta 0 0.25 .5 .75

        middle = 0.125
        if deg < 0.25 - middle and quad % 2 == 0:
            self.tank_angle = 0
            self.x_velocity = SPEED
            self.y_velocity = 0
        elif deg < 0.5 - middle:
            self.tank_angle = 1
            self.x_velocity = SPEED
            self.y_velocity = SPEED/2
        elif deg < 0.75 - middle:
            self.tank_angle = 2
            self.x_velocity = SPEED
            self.y_velocity = SPEED
        elif deg < 1 - middle:
            self.tank_angle = 3
            self.x_velocity = SPEED/2
            self.y_velocity = SPEED
        else:
            self.tank_angle = 4
            self.x_velocity = 0
            self.y_velocity = SPEED

        if quad > 2:
            self.y_velocity = -self.y_velocity
        if quad > 1 and quad < 2 or quad > 3:
            self.x_velocity = -self.x_velocity

        rect = pygame.Rect(self.x + (self.x_velocity * self.direction),
                           self.y + (self.y_velocity * self.direction), self.size, self.size)

        if rect.collidelist(map) < 0:
            self.x += self.x_velocity * self.direction
            self.y += self.y_velocity * self.direction
        
        for bullet in self.bullets:
            bullet.move(map, (0, 0, 0, 0))

    def get_image(self) -> pygame.Surface:
        sub = self.tank_sprite.subsurface(
            (self.tank_angle * self.size, 0, self.size, self.size))

        horizontal = self.x_velocity < 0
        vertical = self.y_velocity < 0
        return pygame.transform.flip(sub, horizontal, vertical)

    def get_rect(self):
        return (self.x, self.y, self.size, self.size)

    def get_coord(self):
        return (self.x, self.y)

    def draw(self, surface:pygame.Surface):
        surface.blit(self.get_image(), self.get_coord())
        for bullet in self.bullets:
            pygame.draw.rect(surface, self.color, bullet.get_rect())

    def random_pos (self, rects):
        while True:
            x = random.randrange(800)
            y = random.randrange(600)
            
            rect = pygame.Rect(x, y, self.size, self.size)
            if rect.collidelist(rects) < 0:
                break


