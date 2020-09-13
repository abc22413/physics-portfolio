import numpy as np
import matplotlib.pyplot as plt
import math

time = np.arange(0,1000,0.5)
#Deine
H = 10000
u_y = 1000
g = -9.81
m = 1000
k = 0.001

v_t = math.sqrt(abs(m*g/k))

y = []
y2 = []
ti = []
for t in time:
    y_new = H + u_y*t + (v_t**2/g)*math.log(abs(math.cosh( (g*t)/(v_t) ) ) )
    y.append(y_new)
    y2.append(H+u_y*t+0.5*g*t**2)
    ti.append(t)
    if y_new<=0.1:
        break

plt.plot(ti, y)
plt.plot(ti,y2)
plt.show()