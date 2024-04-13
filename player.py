import pygame as pg

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 350
        self.y = 700
        self.me = None
        self.jump = True
        self.jump_size = 7
        
    def draw(self):
        player_surf = pg.image.load('sources/dino.png').convert_alpha()

        scale = pg.transform.scale(
                player_surf, (player_surf.get_width() // 6,
                    player_surf.get_height() // 6))
        scale_rect = scale.get_rect(center=(350, 130))
        self.screen.blit(scale, scale_rect)

    def move(self, keys):
        self.jump1(keys)
            
    
    def jump1(self, keys):
        if self.jump:
            if keys[pg.K_SPACE]:
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