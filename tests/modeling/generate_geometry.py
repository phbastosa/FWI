import numpy as np

ns = 5
nr = 200

SPS = np.zeros((ns, 2))
RPS = np.zeros((nr, 2))
XPS = np.zeros((ns, 3))

SPS[:, 0] = np.linspace(6000, 10000, ns) 
SPS[:, 1] = 10.0 

RPS[:, 0] = np.linspace(0, 9950, nr)
RPS[:, 1] = 10.0 

spread = 5950
ds = 1000
dr = 50

XPS[:, 0] = np.arange(ns)
XPS[:, 1] = np.arange(ns)*ds/dr 
XPS[:, 2] = np.arange(ns)*ds/dr + spread/dr + 1 

np.savetxt("../inputs/geometry/modeling_test_SPS.txt", SPS, fmt = "%.2f", delimiter = ",")
np.savetxt("../inputs/geometry/modeling_test_RPS.txt", RPS, fmt = "%.2f", delimiter = ",")
np.savetxt("../inputs/geometry/modeling_test_XPS.txt", XPS, fmt = "%.0f", delimiter = ",")