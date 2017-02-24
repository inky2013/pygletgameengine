import pyglet
import logging
from json import dumps as json_dumps
from engine.components.scene import _DefaultCrashScene


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
        self.scene_manager = _SceneManager()
        self.config = config
        self._saves = {}
        self._window = None
        self.logger = _generate_logger(__name__)
        self.size = [800, 600]

        if config is None:
            config = {'catch_events': False,
                      'crash_scene': _DefaultCrashScene('crash_scene', self),
                      'gl_blending': True}

        if config['gl_blending']:
            pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
            pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
            self.logger.info('Enabled OpenGL Blending')

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
                    if scene.activate() is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_close():
            for scene in self.scene_manager:
                try:
                    if scene.close() is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_context_lost():
            for scene in self.scene_manager:
                try:
                    if scene.context_lost() is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_context_state_lost():
            for scene in self.scene_manager:
                try:
                    if scene.context_state_lost() is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_deactivate():
            for scene in self.scene_manager:
                try:
                    if scene.deactivate()is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_draw(*args):
            for scene in self.scene_manager:
                try:
                    if scene.draw()is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_expose():
            for scene in self.scene_manager:
                try:
                    if scene.expose()is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_hide():
            for scene in self.scene_manager:
                try:
                    if scene.hide()is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_key_press(symbol, modifiers):
            for scene in self.scene_manager:
                try:
                    if scene.key_press(symbol, modifiers)is False: return
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
                    if scene.key_release(*args)is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_drag(*args):
            for scene in self.scene_manager:
                try:
                    if scene.mouse_drag(*args)is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_enter(*args):
            for scene in self.scene_manager:
                try:
                    if scene.mouse_enter(*args)is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_leave(*args):
            for scene in self.scene_manager:
                try:
                    if scene.mouse_leave(*args)is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_motion(*args):
            for scene in self.scene_manager:
                try:
                    if scene.mouse_motion(*args)is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_press(*args):
            for scene in self.scene_manager:
                try:
                    if scene.mouse_press(*args)is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_scroll(*args):
            for scene in self.scene_manager:
                try:
                    if scene.mouse_scroll(*args)is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_mouse_release(*args):
            for scene in self.scene_manager:
                try:
                    if scene.mouse_release(*args)is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_move(*args):
            for scene in self.scene_manager:
                try:
                    if scene.move(*args)is False: return
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
                    if scene.resize(x, y)is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        @self._window.event
        def on_show():
            for scene in self.scene_manager:
                try:
                    if scene.show()is False: return
                except Exception as e:
                    if self.config['catch_events']:
                        self.logger.exception(e)
                    else:
                        raise e

        def update(*args):
            for scene in self.scene_manager:
                try:
                    if scene.update()is False: return
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
