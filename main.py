import pygame as pg
from player import Player
from enemy1 import Enemy1
adfs
class Game: 
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((500,250))
        self.back_surf = pg.image.load('sources/background.jpg')
        self.clock = pg.time.Clock()
        self.player = Player(self.screen)
        self.enemy1 = Enemy1(self.screen)
        self.is_game = True

    def game(self):
        while self.is_game:
            self.draw()
            self.move()
            self.update()
            self.clock.tick(30)

    def draw(self):
        self.screen.blit(self.back_surf, (0,0))
        self.player.draw()
        self.enemy1.draw()

    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        
        keys_pressed = pg.key.get_pressed()
        self.player.move(keys_pressed)
        self.enemy1.move()

    def update(self):
        pg.display.update()
        self.is_game = not self.player.me.colliderect(self.enemy1.enemy_rect)

game = Game()
game.game()