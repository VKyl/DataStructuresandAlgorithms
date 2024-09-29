"""
README BEFORE USE!

If you are working from PyCharm probably you do have
checked option to show plots in tool window ("SciView").
In that case matplotlib animations won't work until you
uncheck this option in your PyCharm Settings -> Tools
                                             -> Python Plots
                                             -> Show plots in tool window
Then start the program as usual, it will display
animation in a separate window called "python".
After you are done, you can check an option back to view
usual plots in SciView.
"""
import functools
import math
import random
import warnings
from simulation import Particle
import heapq
from Event import Event

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# disable warnings
warnings.filterwarnings("ignore")
# matplotlib configuration
# bounds of the room
x_lim = (0, 30)
y_lim = (0, 20)
# scaler for bigger points in plots
PLT_RADIUS_SCALER = 25

# set up plot to draw animations
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=x_lim, ylim=y_lim)
# disable x and y axes labels
ax.set_yticks([])
ax.set_xticks([])


class CollisionSystem:
    def __init__(self, particles: list[Particle]):
        self._particles = particles
        self._sim_time = 0
        self._events = []
        heapq.heapify(self._events)

    def predict(self, particle):
        for that in self._particles:
            time = particle.time_to_hit(that)
            event = Event(self._sim_time + time, particle, that)
            if event.is_valid:
                heapq.heappush(self._events, event)

    def simulate(self, dt):
        scatters = []
        while self._events:
            event = heapq.heappop(self._events)
            print(event.time)
            a: Particle = event.a
            b: Particle = event.b
            if event.is_valid and event.time <= self._sim_time:
                a.bounce_off(b)

        for particle in self._particles:
            particle.move(dt)
            scatters.append(particle.scatter)
            particle.collisions_count = 0
            self.predict(particle)
        self._sim_time += dt
        return scatters


def animate(collision_system: CollisionSystem, dt, _t):
    scatters = collision_system.simulate(dt)

    return scatters


if __name__ == "__main__":
    # 10 milliseconds delta t
    delta_t = 30
    n_balls = 5
    balls = []

    for i in range(n_balls):
        x = random.randint(1, 25)
        y = random.randint(1, 15)
        vx = random.randint(1, 20)
        vy = random.randint(1, 20)
        mass = random.random()
        radius = random.random()
        print(f"Creating a new Particle({x}, {y}, {vx}, {vy}, {radius}, {mass})")

        balls.append(Particle(x, y, vx, vy, radius, mass, ax))
    collision_system = CollisionSystem(balls)

    ani = animation.FuncAnimation(
        fig, functools.partial(animate, collision_system, delta_t / 1_000), interval=delta_t, blit=True, save_count=100,
    )

    plt.show()
