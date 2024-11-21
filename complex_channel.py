import numpy as np

def generate_channel(distance: float, std_s: float, std_m: float, 
                     k: float, n: int, num_ue: int, num_ap: int, num_ant: int):
    
    '''
    Returns a complex channel, in which amplitude is the channel coefficient considering
    path loss, multipath and shadowing effects, and phase is a uniform distribution between
    0 and 2pi.
    
    Parameters
    ----------
    distance : float
        Distance [in m] between ue and the antenna.
    std_s, std_m : float
        Respectively, standard deviation of shadowing effect and multipath effect.
    k: float
        Propagation constant of path loss effect.
    n: int
        Propagation law exponent of path loss effect.
    '''

    amplitude = (
        (np.random.lognormal(sigma = std_s, size = (num_ue, num_ap))) * # Models shadowing effect
        (np.random.rayleigh(std_m, (num_ue, num_ap, num_ant)))**2 *     # Models multipath effect
        (k / distance**n)                                               # Models path loss effect.
    )

    phase = np.random.uniform(0, 2*np.pi, (num_ue, num_ap, num_ant))    # Models phase

    channel = amplitude * np.exp(phase*1j)

    return channel 