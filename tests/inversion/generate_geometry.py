import numpy as np

ns = 21
nr = 100

SPS = np.zeros((ns, 2))
RPS = np.zeros((nr, 2))
XPS = np.zeros((ns, 3))

SPS[:, 0] = np.linspace(500, 4500, ns) 
SPS[:, 1] = 500.0 

RPS[:, 0] = np.linspace(25, 4975, nr)
RPS[:, 1] = 10.0 

XPS[:, 0] = np.arange(ns)

XPS[:, 1] = np.zeros(ns) 
XPS[:, 2] = np.zeros(ns) + nr

np.savetxt("../inputs/geometry/inversion_test_SPS.txt", SPS, fmt = "%.2f", delimiter = ",")
np.savetxt("../inputs/geometry/inversion_test_RPS.txt", RPS, fmt = "%.2f", delimiter = ",")
np.savetxt("../inputs/geometry/inversion_test_XPS.txt", XPS, fmt = "%.0f", delimiter = ",")