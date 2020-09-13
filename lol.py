import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#y = [v, y]
def f(t, y, c):
    dydt = [c[0], y[0]]
    return dydt

tspan = np.linspace(0, 10, 100)
yinit = [10, 0.1]
c = [-9.81]

def event(t, y):
    return y[1]
event.terminal = True

sol = solve_ivp(lambda t, y: f(t, y, c), 
                [tspan[0], tspan[-1]], yinit, events=[event], t_eval=tspan, max_step=0.001)

plt.plot(sol.t, sol.y[1]) #v
plt.plot(sol.t, sol.y[0])
plt.show()

#print(sol.y)