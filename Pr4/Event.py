import math

from simulation import Particle


class Event:
    def __init__(self, time, a: Particle or None, b: Particle or None):
        self._time = time
        self._a: Particle = a
        self._b: Particle = b
        self._a_collisions = a.collisions_count if a else -1
        self._b_collisions = b.collisions_count if b else -1

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def time(self):
        return self._time

    @property
    def is_valid(self):
        return (self.time != math.inf and self.time != -math.inf) and not (self.a.collisions_count or self.b.collisions_count)
        


    def __lt__(self, that: 'Event'):
        return self.time < that.time

    def __gt__(self, that: 'Event'):
        return self.time > that.time

    def __eq__(self, that: 'Event'):
        return self.time == that.time

