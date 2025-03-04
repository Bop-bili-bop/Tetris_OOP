﻿import pygame as pg
from pygame.examples.grid import TILE_SIZE

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32) #302720#

ANIM_TIME_INTERVAL = 150

TILE_SIZE = 45
FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT = 10, 20
FIELD_RES = FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE

INIT_POS_OFFSET = vec(FIELD_WIDTH // 2 - 1, 0)
MOVE_DIRECTIONS = {
    'left': vec(-1, 0),
    'right': vec(1, 0),
    'down': vec(0, 1)
    }

TETROMINOS = {
    'T': [(0,0), (-1,0), (1,0), (0,-1)],
    'O': [(0,0), (0, -1), (1,0), (1,-1)],
    'J': [(0,0), (-1,0), (0, -1), (0,-2)],
    'L': [(0,0), (1,0), (0,-1), (0,-2)],
    'I': [(0,0), (0,1), (0,-1), (0,-2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0,-1), (-1, -1)]
}