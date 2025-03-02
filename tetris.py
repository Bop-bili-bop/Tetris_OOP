from settings import *
import math
from tetromino import Tetromino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)

    def control(self, pressed_key):
        match pressed_key:
            case pg.K_LEFT:
                self.tetromino.move(direction='left')
            case pg.K_RIGHT:
                self.tetromino.move(direction='right')
    def draw_grid(self):
        for x in range(FIELD_WIDTH):
            for y in range(FIELD_HEIGHT):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TILE_SIZE, y * TILE_SIZE,
                             TILE_SIZE, TILE_SIZE), 1)
    def update(self):
        if self.app.anim_trigger:
            self.tetromino.update()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)