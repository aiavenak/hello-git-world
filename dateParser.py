import socket   

import numpy as np
import matplotlib.pyplot as plt

print "-" * 25

hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Your Computer Name is:" + hostname)   
print("Your Computer IP Address is:" + IPAddr)   

print "-" * 25

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


