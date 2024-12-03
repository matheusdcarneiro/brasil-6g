import numpy as np
from matplotlib import pyplot as plt

from complex_channel import *
from positioning import *
from kpi import *
from sim_functions import *

np.random.seed(99)

# Model constants
std_s = 2              # Standard deviation of shadowing
std_m = 1 / np.sqrt(2) # Standard deviation of multipath
k = 10**-4             # Propagation constant of path loss
n = 4                  # Propagation law exponent of path loss

# Model parameters
num_ue = 1
num_ap = 1
num_ant = 4
cov_side = 400
total_bandwidth = 100e6
seeds = 1

# Simulation data
total_snr_sc = np.zeros((num_ue, seeds))

# Monte Carlo simulation
for seed in range(seeds):

    # Positioning UEs and APs
    ue_pos = random_ue_positions(num_ue, cov_side)
    ap_pos = ap_positions(num_ap, cov_side)
    dis = distance(ue_pos, ap_pos)

    # Channel coefficient
    channel, phases = generate_channel(dis, std_s, std_m, k, n, num_ue, num_ap, num_ant) 

    print(channel.shape)

    # SNR with combination by selection
    snr = snr_sc(channel, np.ones(num_ue), power_noise(total_bandwidth))
    snr_ = snr_egc(channel, phases, np.ones(num_ue), power_noise(total_bandwidth))

    total_snr_sc[:, seed] = lin2db(snr)

# Plotting
#snr_sc_ecdf = eCDF(total_snr_sc.flatten())
#plt.plot(snr_sc_ecdf[0], snr_sc_ecdf[1])

#plt.xlabel('SNR [dB]')
#plt.ylabel('eCDF')
#plt.grid()
#plt.show()