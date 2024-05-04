import pygame as pg

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 300
        self.y = 100
        self.jump = True
        self.jump_size = 7
        
    def draw(self):
        player_surf = pg.image.load('sources/dino2.png').convert_alpha()

        scale = pg.transform.scale(
                player_surf, (player_surf.get_width() // 4,
                    player_surf.get_height() // 4))
        scale_rect = scale.get_rect(center=(300, self.y))
        self.me = scale_rect
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