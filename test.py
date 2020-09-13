import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(t, y, c):
    dydt = [c[0] * y[0]]
    return dydt
    
tspan = np.linspace(0, 3, 25)
yinit = [10]
c = [1.02]

def event(t, y, c):
    return y

sol = solve_ivp(lambda t, y: f(t, y, c), 
                [tspan[0], tspan[-1]], yinit, t_eval=tspan)

y_arr = sol.y[0]
x_arr = sol.t

plt.plot(x_arr, y_arr)
plt.show()