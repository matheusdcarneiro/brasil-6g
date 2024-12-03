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
seeds = 10000

# Simulation data
total_snr_sc = np.zeros((num_ue, seeds))
total_snr_egc = np.zeros((num_ue, seeds))
total_snr_mrc = np.zeros((num_ue, seeds))

# Monte Carlo simulation
for seed in range(seeds):

    # Positioning UEs and APs
    ue_pos = random_ue_positions(num_ue, cov_side)
    ap_pos = ap_positions(num_ap, cov_side)
    dis = distance(ue_pos, ap_pos)

    # Channel coefficient
    channel, phases, amp = generate_channel(dis, std_s, std_m, k, n, num_ue, num_ap, num_ant) 

    # SNR with combination by selection
    snr = snr_sc(channel, np.ones(num_ue), power_noise(total_bandwidth))
    snr_ = snr_egc(channel, amp, np.ones(num_ue), power_noise(total_bandwidth))
    snr__ = snr_mrc(channel, np.ones(num_ue), power_noise(total_bandwidth))

    total_snr_sc[:, seed] = lin2db(snr)
    total_snr_egc[:, seed] = lin2db(snr_)
    total_snr_mrc[:, seed] = lin2db(snr__)


# Plotting
snr_sc_ecdf = eCDF(total_snr_sc.flatten())
plt.plot(snr_sc_ecdf[0], snr_sc_ecdf[1], label='Selection combiner (SC)')

snr_egc_ecdf = eCDF(total_snr_egc.flatten())
plt.plot(snr_egc_ecdf[0], snr_egc_ecdf[1], label='Equal Gain Combiner (EGC)')

snr_mrc_ecdf = eCDF(total_snr_mrc.flatten())
plt.plot(snr_mrc_ecdf[0], snr_mrc_ecdf[1], label='Maximum Ration Combiner (MRC)')

plt.xlabel('SNR [dB]')
plt.ylabel('eCDF')
plt.legend()
plt.grid()
plt.show()

plt.save_fig('combiner_eCDF.pdf')