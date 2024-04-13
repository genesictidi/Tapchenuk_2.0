import pygame as pg
from player import Player

class Enemy1:
    def __init__(self, screen):
        self.screen = screen
        self.x = 700
        self.y = 130
        self.target_x = 25
        self.target_y = 200
        self.player = Player(self.screen)
        self.enemy_rect = None

    def draw(self):
        self.enemy_rect = pg.draw.circle(self.screen, 'red', (self.x, self.y), 25)

    def move(self):                         
        if self.x > self.target_x:
            self.x -= 10
        else:
            self.x += 700
        