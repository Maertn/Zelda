import pygame as pg
import sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGTH))
        pg.display.set_caption('Zelda')
        self.clock = pg.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_m:
                        self.level.toggle_menu()

            self.screen.fill('black')
            self.level.run()
            pg.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()