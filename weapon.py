import pygame as pg

class Weapon(pg.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        self.image = pg.Surface((40,40))
        self.rect = self.image.get_rect(center=player.rect.center)
    
    def __str__(self):
        return "weapon"