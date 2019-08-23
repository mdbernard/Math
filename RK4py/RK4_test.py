from RK4py import RK4
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
plt.style.use('dark_background')


def dxdt(x, t):
    return t


x_0 = 1
t_0 = 1
dt = 5

x_1 = RK4(dxdt, x_0, t_0, dt)
print(x_1.val)
