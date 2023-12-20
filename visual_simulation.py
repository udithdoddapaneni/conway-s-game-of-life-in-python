import pygame as pg
from main import count_neighbors, nextgen
import random

pg.init()
screen = pg.display.set_mode((800, 800))

dead = "black"
alive = "white"

WIDTH = 20
HEIGHT = 20


def CreateCell(x,y):

    return pg.Rect(x,y, WIDTH, HEIGHT)

def make_grid(grid):

    display_grid = [[0]*len(grid[0]) for i in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid)):
            display_grid[i][j] = CreateCell(i*WIDTH, j*WIDTH)

    return display_grid

def draw(surface, display_grid, grid):

    for i in range(len(grid)):
        for j in range(len(grid)):
            R = display_grid[i][j]
            if grid[i][j] == 1: # alive
                pg.draw.rect(surface, alive, R)
            else: # dead
                pg.draw.rect(surface, dead, R)

    pg.display.update()



# environment

env_grid = [[0]*40 for i in range(40)]
display_grid = make_grid(env_grid)

# seeding

env_grid[7][7] = 1
env_grid[7][8] = 1
env_grid[7][6] = 1

def simulate():
    global screen, env_grid, display_grid


    screen.fill("green")

    running = True
    clock = pg.time.Clock()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        
        draw(screen, display_grid, env_grid)

        env_grid = nextgen(env_grid)

        clock.tick(2)

    pg.quit()

simulate()