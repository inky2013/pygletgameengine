import pyglet


class Scene:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.z_index = 1

    def activate(self):
        pass

    def close(self):
        pass

    def context_lost(self):
        pass

    def context_state_lost(self):
        pass

    def deactivate(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def expose(self):
        pass

    def hide(self):
        pass

    def key_press(self, key, modifier):
        pass

    def mouse_motion(self, x, y, dx, dy):
        pass

    def mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def mouse_enter(self, x, y):
        pass

    def mouse_leave(self, x, y):
        pass

    def mouse_press(self, x, y, btn, modifier):
        pass

    def mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass

    def mouse_release(self, x, y, button, modifiers):
        pass

    def move(self, x, y):
        pass

    def resize(self, width, height):
        pass

    def show(self):
        pass

    def save(self):
        pass
    
    
class BlockingScene(Scene):
    def activate(self):
        return False

    def close(self):
        return False

    def context_lost(self):
        return False

    def context_state_lost(self):
        return False

    def deactivate(self):
        return False

    def update(self):
        return False

    def draw(self):
        return False

    def expose(self):
        return False

    def hide(self):
        return False

    def key_press(self, key, modifier):
        return False

    def mouse_motion(self, x, y, dx, dy):
        return False

    def mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        return False

    def mouse_enter(self, x, y):
        return False

    def mouse_leave(self, x, y):
        return False

    def mouse_press(self, x, y, btn, modifier):
        return False

    def mouse_scroll(self, x, y, scroll_x, scroll_y):
        return False

    def mouse_release(self, x, y, button, modifiers):
        return False

    def move(self, x, y):
        return False

    def resize(self, width, height):
        return False

    def show(self):
        return False

    def save(self):
        return False


class _DefaultCrashScene(BlockingScene):
    def __init__(self, *args):
        super().__init__(*args)
        self._colours = (244, 67, 54, 255,
                         244, 67, 54, 255,
                         244, 67, 54, 255,
                         244, 67, 54, 255)
        self.crash_title = pyglet.text.Label(text='The Game Has Crashed :(',
                                             x=self.game.size[0]/2,
                                             y=(self.game.size[1]/2)+(self.game.size[1]/20),
                                             anchor_x='center',
                                             anchor_y='center',
                                             font_name='consolas',
                                             font_size=self.game.size[0]/20)
        self.crash_desc = pyglet.text.Label(text='All available game data was saved',
                                             x=self.game.size[0] / 2,
                                             y=(self.game.size[1] / 2) - (self.game.size[1]/20),
                                             anchor_x='center',
                                             anchor_y='center',
                                             font_name='consolas',
                                             font_size=self.game.size[0] / 40)

    def activate(self):
        self.game.save()
        return False

    def resize(self, width, height):
        self.crash_title.font_size = width/20
        self.crash_desc.font_size = width/40
        self.crash_title.x = width/2
        self.crash_desc.x = width/2
        self.crash_title.y = (height/2)+(width/20)
        self.crash_desc.y = (height/2)-(width/20)
        return False

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', [
                                 0, 0,
                                 self.game.size[0], 0,
                                 self.game.size[0], self.game.size[1],
                                 0, self.game.size[1]
                             ]),
                             ('c4B', self._colours))
        self.crash_title.draw()
        self.crash_desc.draw()
        return False
