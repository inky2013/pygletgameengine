import engine
import pyglet
from copy import copy
from random import randint

print(dir(engine))

game = engine.Engine()


class TestScene(engine.components.scene.Scene):
    def __init__(self, game):
        super().__init__('testscene', game)
        self._ALPHA = 100
        self.z_index = 1
        self._colours = [0, 0, 0, self._ALPHA, 0, 0, 0, self._ALPHA, 0, 0, 0, self._ALPHA, 0, 0, 0, self._ALPHA]
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
                self._colours_target.append(self._ALPHA)
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

game.scene_manager['test'] = TestScene(game)

game.scene_manager['button'] = engine.components.buttons.Button(game, 'btn', 100, 100, 100, 40, 'hello', 5, action=lambda: print('callback'))

game.present(resizable=True)
