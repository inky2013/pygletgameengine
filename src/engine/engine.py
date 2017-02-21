import pyglet
import logging
from json import dumps as json_dumps
from engine.scene import _DefaultCrashScene


class _Event:
    def __init__(self):
        self._is_propagating_event = True

    def stop_propegation(self):
        self._is_propagating_event = False

    def is_propagating_event(self):
        return self._is_propagating_event


class _SceneManager:
    def __init__(self):
        self._scenes = []

    def clear(self):
        self._scenes = []

    def __iter__(self):
        for item in self._scenes:
            yield item

    def __setitem__(self, name, value):
        value.name = name
        self._scenes.append(value)
        self._scenes.sort(key=lambda x: x.z_index, reverse=False)

    def __delitem__(self, key):
        for item in self._scenes:
            if item.name == key:
                del item

    def __getitem__(self, key):
        for i in self._scenes:
            if i.name == key:
                return i
        return None


class Engine:
    def __init__(self, config=None):
        if config is None:
            config = {'catch_events': False, 'crash_scene': None}
        self.scene_manager = _SceneManager()
        self.config = config
        self._saves = {}
        self._window = None
        self.logger = _generate_logger(__name__)
        self.size = [800, 600]

    def add_save_object(self, obj, jsonfile=None):
        self._saves[obj] = jsonfile

    def save(self):
        for key in self._saves:
            json = key.save()
            if (key is not None) and (type(json).__name__ == 'dict'):
                f = open(self._saves[key], 'w+')
                f.write(json_dumps(json))
                f.close()

    def crash(self):
        self.scene_manager.clear()
        cscene = None
        if self.config['crash_scene'] is not None:
            cscene = self.config['crash_scene']
        else:
            cscene = _DefaultCrashScene('crash', self)
        self.scene_manager['crash'] = cscene


    def present(self, x=800, y=600, fps=60, resizable=False, fullscreen=False):
        self.size = [x, y]
        self._window = pyglet.window.Window(width=x, height=y, resizable=resizable, fullscreen=fullscreen)

        @self._window.event
        def on_activate():
            for scene in self.scene_manager:
                try:
                    if not scene.activate(): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_close():
            for scene in self.scene_manager:
                try:
                    if not scene.close(): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_context_lost():
            for scene in self.scene_manager:
                try:
                    if not scene.context_lost(): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_context_state_lost():
            for scene in self.scene_manager:
                try:
                    if not scene.context_state_lost(): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_deactivate():
            for scene in self.scene_manager:
                try:
                    if not scene.deactivate(): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_draw(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.draw(): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_expose():
            for scene in self.scene_manager:
                try:
                    if not scene.expose(): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_hide():
            for scene in self.scene_manager:
                try:
                    if not scene.hide(): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_key_press(symbol, modifiers):
            for scene in self.scene_manager:
                try:
                    if not scene.key_press(symbol, modifiers): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e
            if symbol == pyglet.window.key.ESCAPE:
                return pyglet.event.EVENT_HANDLED

        @self._window.event
        def on_key_release(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.key_release(*args): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_drag(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.mouse_drag(*args): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_enter(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.mouse_enter(*args): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_leave(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.mouse_leave(*args): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_motion(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.mouse_motion(*args): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_press(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.mouse_press(*args): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_scroll(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.mouse_scroll(*args): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_release(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.mouse_release(*args): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_move(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.move(*args): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_resize(x, y):
            if x < 2:
                self._window.width = 2
            if y < 2:
                self._window.height = 2
            self.size = [x, y]
            for scene in self.scene_manager:
                try:
                    if not scene.resize(x, y): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_show():
            for scene in self.scene_manager:
                try:
                    if not scene.show(): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        def update(*args):
            for scene in self.scene_manager:
                try:
                    if not scene.update(): return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        if fps is not None:
            pyglet.clock.schedule_interval(update, 1 / float(fps))
            pyglet.clock.schedule_interval(on_draw, 1 / float(fps))

        pyglet.app.run()


def _generate_logger(name: str, log_level: str="INFO") -> logging.Logger:
    logger = logging.getLogger(name)
    log_level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(log_level)
    fmt = '[%(asctime)s] [%(module)s/%(levelname)s]: %(message)s'
    fmt_date = '%H:%M:%S'
    formatter = logging.Formatter(fmt, fmt_date)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
