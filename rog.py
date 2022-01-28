## imports

import pygame as pg
from random import randint
from itertools import product
import numpy as np

## constantes

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = 20
PIXEL_SIZE = 20

## affichage de caractères
def draw_char(text, position, font, color=BLACK, background=WHITE):
    return font.render(text, False, color, background), position

## initialisation de la MAP

MAP = np.full((20,20), None)

# |
MAP[3:20, 13] = '|'
MAP[3:20, 17] = '|'
MAP[:8, 0] = '|'
MAP[:8, 7] = '|'
MAP[15:20, 0] = '|'
MAP[15:20, 10] = '|'
MAP[7:12, 9] = '|'
MAP[7:12, 12] = '|'
MAP[10:13, 0] = '|'
MAP[10:13, 3] = '|'

# - 
MAP[0][:8] = '-'
MAP[7][:8] = '-'
MAP[10][:4] = '-'
MAP[12][:4] = '-'
MAP[15][:11] = '-'
MAP[19][:11] = '-'
MAP[3][13:18] = '-'
MAP[19][13:18] = '-'
MAP[7][14:17] = '-'
MAP[7, 9:13] = '-'
MAP[11, 9:13] = '-'

# sol
MAP[1:7, 1:7] = '.'
MAP[11, 1:3] = '.'
MAP[16:19, 1:10] = '.'
MAP[4:7, 14:17] = '.'
MAP[8:20, 14:18] = '.'
MAP[8:11, 10:12] = '.'
MAP[7, 15] = '.'

# chemin
MAP[8:11, 5] = '#'
MAP[11, 4:7] = '#'
MAP[11:15, 6] = '#'
MAP[17, 11:13] = '#'
MAP[2:17, 12] = '#'
MAP[2, 13:16] = '#'

# porte
MAP[7, 5] = '+'
MAP[11, 3] = '+'
MAP[15, 6] = '+'
MAP[17, 13] = '+'
MAP[3, 15] = '+'


## initialisation de la fenêtre

pg.init()
screen= pg.display.set_mode((SIZE * PIXEL_SIZE, SIZE * PIXEL_SIZE))
screen.fill(WHITE)
pg.display.flip()

## initialisation de la police
font_arial = pg.font.SysFont('arial', 20)

## jeu
running = True
caption = 'Play ROG game'

while running:
    # affichage plateau de jeu
    for i, j in product(range(SIZE), range(SIZE)):
        if MAP[i,j]:
            # what the fuck
            img, pos = draw_char(MAP[i,j], (j*PIXEL_SIZE, i*PIXEL_SIZE), font=font_arial)
            screen.blit(img, pos)
    # affichage messages
    if caption:
        pg.display.set_caption(caption)
        pg.display.flip()
    # itération sur tous les événements
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.update()


pg.quit()