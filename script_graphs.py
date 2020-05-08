import matplotlib.pyplot as plt
from conjecture_functions import *

N = 100000

x = range(1, N+1)
y = vect_flight(x)
z = vect_rise(x)

plt.subplot(121)
plt.title('time-of-flight')
plt.scatter(x, y, s=3)

plt.subplot(122)
plt.title('time-of-rise')
plt.scatter(x, z, s=3)
plt.show()

