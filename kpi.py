import numpy as np

def snr_sc(channel: float, power_vec: float, n_power: float):
    '''
    Returns the SNR vector after combining by selection, in which is selected only the
    antenna with best SNR.

    Parameters
    ----------
    channel : float
        Channel coefficient matrix [in linear] between an UE and the antennas of each AP.
    power_vec : float
        Transmission power vector [in W] of each UE.
    n_power: float
        Noise power [in W].
    '''

    num_ue, num_ap, num_ant = channel.shape 
    snr_vector = np.zeros(num_ue)

    for ue in range(num_ue):

        for ap in range(num_ap):

            # DO A AP-UE ASSOCIATION (IT IS NOT D-MIMO YET)!

            snr_ant = np.zeros(num_ant)

            for ant in range(num_ant):

                # snr in each antenna
                snr_ant[ant] = (np.absolute(channel[ue, ap, ant]) *
                               (power_vec[ue] / n_power))**2   

            # snr of each ue as the maximum snr antenna
            snr_vector[ue] = np.max(snr_ant)

    return snr_vector

def snr_egc(channel: float, amp: float, power_vec: float, n_power: float):
    '''
    Returns the SNR vector after combining by same gain, in which the weight compensates
    the phase.

    Parameters
    ----------
    channel : float
        Channel coefficient matrix [in linear] between an UE and the antennas of each AP.
    amplitude: float
        Channel amplitude component between and UE.
    power_vec : float
        Transmission power vector [in W] of each UE.
    n_power: float
        Noise power [in W].
    '''

    num_ue, num_ap, num_ant = channel.shape # refers the channel
    snr_vector = np.zeros(num_ue)

    for ue in range(num_ue):

        for ap in range(num_ap):

            # DO A AP-UE ASSOCIATION (IT IS NOT D-MIMO YET)!

            amplitude = amp[ue, ap, :]

            if ((((np.sum(amplitude))**2) / num_ant) * (power_vec[ue] / n_power)**2) == 0:
                print('zerou')

            snr_vector[ue] = (((np.absolute(np.sum(amplitude))**2) / num_ant) * 
                             (power_vec[ue] / n_power)**2)

    return snr_vector

def snr_mrc(channel: float, power_vec: float, n_power: float):
    '''
    Returns the SNR vector after combining by maximum ratio, in which the weight compensates de 
    phase and maximize the amplitude.

    Parameters
    ----------
    channel : float
        Channel coefficient matrix [in linear] between an UE and the antennas of each AP.
    power_vec : float
        Transmission power vector [in W] of each UE.
    n_power: float
        Noise power [in W].
    '''

    num_ue, num_ap, num_ant = channel.shape 
    snr_vector = np.zeros(num_ue)

    for ue in range(num_ue):

        for ap in range(num_ap):

            # DO A AP-UE ASSOCIATION (IT IS NOT D-MIMO YET)!

            snr_ant = np.zeros(num_ant)

            for ant in range(num_ant):

                # snr in each antenna
                snr_ant[ant] = (np.absolute(channel[ue, ap, ant]) *
                               (power_vec[ue] / n_power))**2   

            # snr of each ue as the sum of snr antenna
            snr_vector[ue] = np.sum(snr_ant)

    return snr_vector