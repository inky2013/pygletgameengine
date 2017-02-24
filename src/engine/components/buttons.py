import pyglet
from engine.components.scene import Scene


class Button(Scene):
    def __init__(self, game, name, x, y, w, h, text, z_index=0, font_name='consolas', font_size=20, box_colour=(255,0,0,0, 0,255,0,255, 0,0,255,0, 255,0,255,255), action=lambda: None):
        super().__init__(name, game)
        self.z_index = z_index
        self.box_colour = box_colour
        self.x, self.y, self.width, self.height = x, y, w, h
        self.run_action = action
        self.label = pyglet.text.Label(text=text, anchor_x='center', anchor_y='center', font_size=font_size, font_name=font_name)
        self.label.x = x
        self.label.y = y

    def draw(self):
        x, y = self.x-self.width/2, self.y-self.height/2
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', [
                                 x, y,
                                 x+self.width, y,
                                 x+self.width, y+self.height,
                                 x, y+self.height
                             ]),
                             ('c4B', self.box_colour))
        self.label.draw()

    def mouse_press(self, cx, cy, btn, modifier):
        x, y = self.x - self.width / 2, self.y - self.height / 2
        if (x <= cx) and (x+self.width >= cx) and (y <= cy) and (y+self.height >= cy):
            self.run_action()
        return False
