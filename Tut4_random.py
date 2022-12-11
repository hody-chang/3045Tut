import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import random

length, width = 100, 100

grids = np.zeros((length, width))
current_x, current_y = 0, 0
grids[current_x, current_y] = 1

xdata, ydata = [], []
dis = 0

def movement(direction):
    global grids, current_x, current_y, length, width, dis
    # grids[current_x, current_y] = 0
    if direction == 0:
        current_x, current_y = current_x - 1, current_y
    elif direction == 1:
        current_x, current_y = current_x + 1, current_y  # input your code
    elif direction == 2:
        current_x, current_y = current_x, current_y - 1  # input your code
    elif direction == 3:
        current_x, current_y = current_x, current_y + 1  # input your code
    else:
        pass
        # stay
    if current_x >= length:
        current_x = length - 1 - (current_x - (length - 1))
    elif current_x < 0:
        current_x = - current_x
    else:
        pass
    if current_y >= width:
        current_y = width - 1 - (current_y - (width - 1))
    elif current_y < 0:
        current_y = - current_y
    else:
        pass
    grids[current_x, current_y] += 1
    dis = np.sqrt(current_x**2 + current_y**2)


# initialize the position of the object
plt.figure()
fig = plt.gcf()
ax = plt.gca()
ax_update = ax.imshow(grids, vmin=0, vmax=15)


def run(i):
    global grids, xdata, ydata, ax_update
    movement(random.randint(0, 4))
    ax_update.set_data(grids)
    xdata.append(i)
    ydata.append(dis)
    return ax_update
    

ani = animation.FuncAnimation(fig, run, interval = 10)

plt.show()
plt.plot(xdata,ydata)
plt.xlabel("Time t")
plt.ylabel("Distance")
plt.show()


