import engine
import pyglet
from copy import copy
from random import randint

game = engine.Engine()

class Particle(pyglet.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(img=pyglet.image.load('assets/sparkle.png'), x=x, y=y)
        self.life = 0

class TestScene(engine.Scene):
    def __init__(self):
        super().__init__('testscene')
        self.z_index = 1
        self._colours = [0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255]
        self._colours_target = copy(self._colours)
        self._particles = []

    @staticmethod
    def get_amt(i, target):
        if i > target:
            return -1
        elif i < target:
            return 1
        else:
            return 0

    def update(self):
        if self._colours == self._colours_target:
            self._colours_target = []
            for x in range(4):
                for y in range(3):
                    self._colours_target.append(randint(1, 255))
                self._colours_target.append(255)
        else:
            for x in range(len(self._colours)):
                self._colours[x] += self.get_amt(self._colours[x], self._colours_target[x])


    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', [
                                 0, 0,
                                 game.size[0], 0,
                                 game.size[0], game.size[1],
                                 0, game.size[1]
                             ]),
                             ('c4B', self._colours))

game.scene_manager['test'] = TestScene()

game.present(resizable=True)