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

MAX_SPEED = 20
class Particle:
    def __init__(self, rx, ry, vx, vy, radius, mass, ax):
        self._rx = rx
        self._ry = ry
        self._vx = vx
        self._vy = vy
        self._radius = radius
        self._mass = mass
        self._collisions_count = 0
        self.ax = ax
        self._scatter, = self.ax.plot([], [], 'o', markersize=self._radius * PLT_RADIUS_SCALER)

    @property
    def rx(self):
        return self._rx

    @property
    def ry(self):
        return self._ry

    @property
    def vx(self):
        return self._vx

    @property
    def vy(self):
        return self._vy

    @vx.setter
    def vx(self, value):
        self._vx = value

    @vy.setter
    def vy(self, value):
        self._vy = value

    @property
    def radius(self):
        return self._radius

    @property
    def mass(self):
        return self._mass

    @property
    def collisions_count(self):
        return self._collisions_count

    @collisions_count.setter
    def collisions_count(self, value):
        self._collisions_count = value

    @property
    def scatter(self):
        return self._scatter

    def move(self, dt):
        if (self._rx + self._vx * dt < x_lim[0] + self._radius) or \
                (self._rx + self._vx * dt > x_lim[1] - self._radius):
            self._vx = -self._vx
        if (self._ry + self._vy * dt < y_lim[0] + self._radius) or \
                (self._ry + self._vy * dt > y_lim[1] - self._radius):
            self._vy = -self._vy
        self._vx = min(self._vx, MAX_SPEED)
        self._vy = min(self._vy, MAX_SPEED)

        self._rx = self._rx + self._vx * dt
        self._ry = self._ry + self._vy * dt
        self.scatter.set_data([self._rx], [self._ry])

    def bounce_off(self, that):
        dx = that.rx - self.rx
        dy = that.ry - self.ry
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx * dvx + dy * dvy
        dist = self.radius + that.radius
        j = 2 * self.mass * that.mass * dvdr / ((self.mass + that.mass) * dist)
        j_x = j * dx / dist
        j_y = j * dy / dist
        self.vx += j_x / self.mass
        self.vy += j_y / self.mass
        that.vx -= j_x / that.mass
        that.vy -= j_y / that.mass
        self.vx, self.vy = min(self.vx, MAX_SPEED), min(self.vy, MAX_SPEED)
        that.vx, that.vy = min(that.vx, MAX_SPEED), min(that.vy, MAX_SPEED)
        self.collisions_count += 1
        that.collisions_count += 1

    def time_to_hit(self, that):
        if self == that:
            return math.inf
        dx = that.rx - self.rx
        dy = that.ry - self.ry
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx * dvx + dy * dvy
        if dvdr > 0:
            return math.inf
        dvdv = dvx * dvx + dvy * dvy
        drdr = dx * dx + dy * dy
        sigma = self.radius + that.radius
        d = (dvdr * dvdr) - dvdv * (drdr - sigma * sigma)
        if d < 0:
            return math.inf
        if dvdv != 0:
            return -(dvdr + math.sqrt(d)) / dvdv
        return math.inf



# this function moves all objects passing delta time, returns
# scatter plot of points that should be drawn
# the last parameter is time in seconds, it goes from matplotlib animator
def animate(objects, dt, _t):
    for obj in objects:
        obj.move(dt)

    return [obj.scatter for obj in objects]


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
        radius = random.randint(3,5)
        print(f"Creating a new Particle({x}, {y}, {vx}, {vy}, {radius}, {mass})")
        balls.append(Particle(x, y, vx, vy, radius, mass, ax))

    ani = animation.FuncAnimation(
        fig, functools.partial(animate, balls, delta_t / 1_000), interval=delta_t, blit=True, save_count=100,
    )

    plt.show()
