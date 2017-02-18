import pyglet
import logging




class Engine:
    def __init__(self):
        self._scenestack = []
        self._window = pyglet.window.Window(width=800, height=600)
        self.logger = _generate_logger(__name__)

    def add_scene(self, sceneobj):
        self._scenestack.append(sceneobj)
        # Sort the scene stack according to z_index value
        self._scenestack.sort(key=lambda x: x.z_index, reverse=False)

    def present(self, x=800, y=600, fps=60):
        self._window.height = y
        self._window.width = x

        @self._window.event
        def on_activate():
            for scene in self._scenestack:
                try:
                    scene.activate()
                except Exception as e:
                    self.logger.exception(e)

        def on_close():
            for scene in self._scenestack:
                try:
                    scene.close()
                except Exception as e:
                    self.logger.exception(e)

        def on_context_lost():
            for scene in self._scenestack:
                try:
                    scene.context_lost()
                except Exception as e:
                    self.logger.exception(e)

        def on_context_state_lost():
            for scene in self._scenestack:
                try:
                    scene.context_state_lost()
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_deactivate():
            for scene in self._scenestack:
                try:
                    scene.deactivate()
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_draw():
            for scene in self._scenestack:
                try:
                    scene.draw()
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_expose():
            for scene in self._scenestack:
                try:
                    scene.expose()
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_hide():
            for scene in self._scenestack:
                try:
                    scene.hide()
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_key_press(symbol, modifiers):
            for scene in self._scenestack:
                try:
                    scene.key_press(symbol, modifiers)
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_key_release(symbol, modifiers):
            pass

        @self.game_window.event
        def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
            pass

        @self.game_window.event
        def on_mouse_enter(x, y):
            pass

        @self.game_window.event
        def on_mouse_leave(x, y):
            pass

        @self.game_window.event
        def on_mouse_motion(x, y, dx, dy):
            pass

        @self.game_window.event
        def on_mouse_press(x, y, button, modifiers):
            pass

        @self.game_window.event
        def on_mouse_scroll(x, y, scroll_x, scroll_y):
            pass

        @self.game_window.event
        def on_mouse_release(x, y, button, modifiers):
            pass

        @self.game_window.event
        def on_move(x, y):
            pass

        @self.game_window.event
        def on_resize(width, height):
            pass

        @self.game_window.event
        def on_show():
            pass

        def update(*args):
            pass

        if fps is not None:
            pyglet.clock.schedule_interval(update, 1 / float(fps))

        pyglet.app.run()

def _generate_logger(name:str, loglevel:str="INFO") -> logging.Logger:
    logger = logging.getLogger(name)
    loglevel = getattr(logging, loglevel.upper(), logging.INFO)
    logger.setLevel(loglevel)
    fmt = '[%(asctime)s] [%(module)s/%(levelname)s]: %(message)s'
    fmt_date = '%H:%M:%S'
    formatter = logging.Formatter(fmt, fmt_date)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger