

import numpy as np

def bolt():
  k1,k2,k3,v = input().split()
  k1,k2,k3,v = float(k1),float(k2),float(k3),float(v)
  distance = 100
  speed = k1*k2*k3*v
  time = np.round(distance/speed,2)
  if time < 9.58:
    print("Yes")
  else: print("No")

t = int(input().strip())
for t in range(0,t):
  bolt()