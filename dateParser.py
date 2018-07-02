import socket   

import numpy as np
import matplotlib.pyplot as plt

print "-" * 15
print "computer name and IP address Example"
print "-" * 15

hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Your Computer Name is:" + hostname)   
print("Your Computer IP Address is:" + IPAddr)   

print "-" * 15
print "How to plot simple functions"
print "-" * 15

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


