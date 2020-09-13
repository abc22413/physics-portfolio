import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#y = [a, v, x]
def f(t, y, c):
    dydt = [-c[0]*y[2]/c[1], y[0], y[1]]
    return dydt

tspan = np.linspace(0, 10, 100*10)
yinit = [0, 0, 10]
#[k,m]
c = [1,1]

sol = solve_ivp(lambda t, y: f(t, y, c), 
                [tspan[0], tspan[-1]], yinit, t_eval=tspan)

plt.plot(sol.t, sol.y[2]) #x
#plt.plot(sol.t, sol.y[0])
plt.show()

#print(sol.y)