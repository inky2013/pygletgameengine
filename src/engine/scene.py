

class Scene:
    def __init__(self, name, game):
        self.name = name
        self.game = game

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

    def mouse_drag(self, x, y, dx, dy):
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
