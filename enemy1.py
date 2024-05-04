import pygame as pg
from player import Player

class Enemy1:
    def __init__(self, screen):
        self.screen = screen
        self.x = 700
        self.y = 100
        self.target_x = 25
        self.target_y = 200
        self.player = Player(self.screen)
        

    def draw(self):
        #self.enemy_rect = pg.draw.circle(self.screen, 'red', (self.x, self.y), 25)
        enemy1_surf = pg.image.load('sources/cactus.png').convert_alpha()

        scale = pg.transform.scale(
                enemy1_surf, (enemy1_surf.get_width() // 4,
                    enemy1_surf.get_height() // 4))
        scale_rect = scale.get_rect(center=(self.x, 100))
        self.me = scale_rect
        self.screen.blit(scale, scale_rect)

    def move(self):                         
        if self.x > self.target_x:
            self.x -= 9
        else:
            self.x += 700
        