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


class Ball:
    def __init__(self, rx, ry, vx, vy, radius):
        self._rx = rx
        self._ry = ry
        self._vx = vx
        self._vy = vy
        self._radius = radius

        # scatter plot for drawing point
        self.scatter, = ax.plot([], [], 'o', markersize=self._radius * PLT_RADIUS_SCALER)

    def move(self, dt):
        if (self._rx + self._vx * dt < x_lim[0] + self._radius) or \
                (self._rx + self._vx * dt > x_lim[1] - self._radius):
            self._vx = -self._vx

        if (self._ry + self._vy * dt < y_lim[0] + self._radius) or \
                (self._ry + self._vy * dt > y_lim[1] - self._radius):
            self._vy = -self._vy

        self._rx = self._rx + self._vx * dt
        self._ry = self._ry + self._vy * dt

        # updates point position in plot
        self.scatter.set_data([self._rx], [self._ry])


# this function moves all objects passing delta time, returns
# scatter plot of points that should be drawn
# the last parameter is time in seconds, it goes from matplotlib animator
def animate(objects, dt, _t):
    for obj in objects:
        obj.move(dt)

    return [obj.scatter for obj in objects]


if __name__ == "__main__":
    # 10 milliseconds delta t
    delta_t = 10
    n_balls = 5
    balls = []

    for i in range(n_balls):
        x = random.randint(1, 25)
        y = random.randint(1, 15)
        vx = random.randint(1, 20)
        vy = random.randint(1, 20)
        radius = random.random()
        print(f"Creating a new Ball({x}, {y}, {vx}, {vy}, {radius})")
        balls.append(Ball(x, y, vx, vy, radius))

    # interval in milliseconds
    ani = animation.FuncAnimation(
        fig, functools.partial(animate, balls, delta_t / 1_000),
        interval=delta_t, blit=True, save_count=100,
    )

    plt.show()
