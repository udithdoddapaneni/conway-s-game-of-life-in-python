import pygame as pg
from simulation_logic import nextgen

pg.init()
screen = pg.display.set_mode((800, 850))
font = pg.font.SysFont('didot.ttc', 60)
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
                pg.draw.rect(surface, alive, R, border_radius=2)
            else: # dead
                pg.draw.rect(surface, dead, R, border_radius=2)

#button = pg.Rect()

# environment

env_grid = [[0]*40 for i in range(40)]
display_grid = make_grid(env_grid)

# seeding


RESET = pg.Rect(200, 800, 200, 50)
START = pg.Rect(0, 800, 200, 50)
start_text = font.render('START', True, 'green')
reset_text = font.render('RESET', True, 'green')

def reset():
    global env_grid

    for i in range(len(env_grid)):
        for j in range(len(env_grid[0])):
            env_grid[i][j] = 0


def simulate():
    global screen, env_grid, display_grid

    FPS = 60
    start = False
    screen.fill("purple")
    pg.draw.rect(screen, "blue", START)
    pg.draw.rect(screen, "yellow", RESET)
    screen.blit(start_text, (30, 810))
    screen.blit(reset_text, (230, 810))
    running = True
    clock = pg.time.Clock()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                i = pos[0]//20
                j = pos[1]//20
                if START.collidepoint(pos) and not start:
                    FPS = 5
                    start = True
                    pg.draw.rect(screen, "red", START)
                    screen.blit(start_text, (30, 810))
                elif RESET.collidepoint(pos):
                    FPS = 60
                    start = False
                    pg.draw.rect(screen, "blue", START)
                    screen.blit(start_text, (30, 810))
                    reset()
                elif i < len(env_grid) and j < len(env_grid[0]) and not start:
                    if env_grid[i][j]:
                        env_grid[i][j] = 0
                    else:
                        env_grid[i][j] = 1
                    
        
        draw(screen, display_grid, env_grid)
        pg.display.update()
        if start:
            env_grid = nextgen(env_grid)

        clock.tick(FPS)

    pg.quit()

simulate()
