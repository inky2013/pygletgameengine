

class Clickable:
    def is_in_bounds(self, x, y):
        if (self.x > x) and (self.x+self.width < x) and (self.y < y) and (self.y+self.height < y):
            return True
        return False

    def run_action(self):
        print('Override the run_action() function of %s' % str(self))