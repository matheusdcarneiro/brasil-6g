import numpy as np
from complex_channel import *

distance = 100
std_s = 2
std_m = 1 / np.sqrt(2)
k = 10**-4
n = 4

print(generate_channel(distance, std_s, std_m, k, n, 2, 2, 2))