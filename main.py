import pygame as pg
from collections import deque
from random import choice, randrange


class Ant:
    def __init__(self, app, pos, color):
        self.app = app
        self.color = color
        self.x, self.y = pos
        self.increments = deque([(1,0), (0,1), (-1,0), (0,-1)])

    def run(self):
        value = self.app.grid[self.y][self.x]
        self.app.grid[self.y][self.x] = not value

        SIZE = self.app.CELL_SIZE
        rect = self.x * SIZE, self.y * SIZE, SIZE - 1, SIZE - 1
        # if value:
        #     pg.draw.rect(self.app.screen, pg.Color('white'), rect)
        # else:
        #     pg.draw.rect(self.app.screen, self.color, rect)

        center = self.x * SIZE, self.y * SIZE
        if value:
            pg.draw.circle(self.app.screen, self.color, center, SIZE)

        self.increments.rotate(1) if value else self.increments.rotate(-1)
        dx, dy = self.increments[0]
        self.x = (self.x + dx) % self.app.COLS
        self.y = (self.y + dy) % self.app.ROWS


class App:
    def __init__(self, WIDTH=1200, HEIGHT=780, CELL_SIZE = 4):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()

        self.CELL_SIZE = CELL_SIZE
        self.ROWS, self.COLS = HEIGHT//CELL_SIZE, WIDTH//CELL_SIZE
        self.grid = [[0 for col in range(self.COLS)] for row in range(self.ROWS)]

        # self.ant1 = [Ant(app=self, pos=[randrange(self.COLS), randrange(self.ROWS)], color=pg.Color('red')) for i in range(50)]
        self.ants = [Ant(app=self, pos=[randrange(self.COLS), randrange(self.ROWS)], color=self.get_color()) for i in range(5000)]
        # self.ants = self.ant1 + self.ants

    @staticmethod
    def get_color():
        channel = lambda x,y: randrange(x, y)
        return channel(100,200), channel(30,40), channel(50,80)

    def run(self):
        while True:
            [ant.run() for ant in self.ants]

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick()

if __name__ == '__main__':
    app = App()
    app.run()