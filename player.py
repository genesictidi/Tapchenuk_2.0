import pygame as pg

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 250
        self.y = 200
        self.me = None
        self.jump = False
        self.jump_size = 7
        
    def draw(self):
        self.me = pg.draw.circle(self.screen, 'black', (self.x, self.y), 25)

    def move(self, keys):
        if keys[pg.K_a]:
            self.x -= 10
        if keys[pg.K_d]:
            self.x += 10
        self.jump1(keys)
            
    
    def jump1(self, keys):
        if self.jump and keys[pg.K_SPACE]:
            self.jump = False
        else:
            if self.jump_size >= -7:
                if self.jump_size > 0:
                    self.y -= self.jump_size**2
                else:
                    self.y += self.jump_size ** 2
                self.jump_size -= 1
            else:
                self.jump = True
                self.jump_size = 7

    def update(self):
        pass