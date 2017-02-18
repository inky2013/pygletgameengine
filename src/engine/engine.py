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
                    if not scene.activate(): return
                except Exception as e:
                    self.logger.exception(e)

        def on_close():
            for scene in self._scenestack:
                try:
                    if not scene.close(): return
                except Exception as e:
                    self.logger.exception(e)

        def on_context_lost():
            for scene in self._scenestack:
                try:
                    if not scene.context_lost(): return
                except Exception as e:
                    self.logger.exception(e)

        def on_context_state_lost():
            for scene in self._scenestack:
                try:
                    if not scene.context_state_lost(): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_deactivate():
            for scene in self._scenestack:
                try:
                    if not scene.deactivate(): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_draw():
            for scene in self._scenestack:
                try:
                    if not scene.draw(): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_expose():
            for scene in self._scenestack:
                try:
                    if not scene.expose(): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_hide():
            for scene in self._scenestack:
                try:
                    if not scene.hide(): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_key_press(symbol, modifiers):
            for scene in self._scenestack:
                try:
                    if not scene.key_press(symbol, modifiers): return
                except Exception as e:
                    self.logger.exception(e)
            if symbol == pyglet.window.key.ESCAPE:
                return pyglet.event.EVENT_HANDLED

        @self.game_window.event
        def on_key_release(*args):
            for scene in self._scenestack:
                try:
                    if not scene.key_release(*args): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_mouse_drag(*args):
            for scene in self._scenestack:
                try:
                    if not scene.mouse_drag(*args): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_mouse_enter(*args):
            for scene in self._scenestack:
                try:
                    if not scene.mouse_enter(*args): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_mouse_leave(*args):
            for scene in self._scenestack:
                try:
                    if not scene.mouse_leave(*args): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_mouse_motion(*args):
            for scene in self._scenestack:
                try:
                    if not scene.mouse_motion(*args): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_mouse_press(*args):
            for scene in self._scenestack:
                try:
                    if not scene.mouse_press(*args): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_mouse_scroll(*args):
            for scene in self._scenestack:
                try:
                    if not scene.mouse_scroll(*args): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_mouse_release(*args):
            for scene in self._scenestack:
                try:
                    if not scene.mouse_release(*args): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_move(*args):
            for scene in self._scenestack:
                try:
                    if not scene.move(*args): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_resize(*args):
            for scene in self._scenestack:
                try:
                    if not scene.resize(*args): return
                except Exception as e:
                    self.logger.exception(e)

        @self.game_window.event
        def on_show():
            for scene in self._scenestack:
                try:
                    if not scene.show(): return
                except Exception as e:
                    self.logger.exception(e)

        def update(*args):
            for scene in self._scenestack:
                try:
                    if not scene.update(*args): return
                except Exception as e:
                    self.logger.exception(e)

        if fps is not None:
            pyglet.clock.schedule_interval(update, 1 / float(fps))
            pyglet.clock.schedule_interval(on_draw, 1 / float(fps))

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