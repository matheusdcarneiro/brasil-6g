import numpy as np

def gen_constellation(num_points):
    '''
    Returns the complex points coordenates of a constellation.

    Parameters
    ----------
    num_points : int
        Number of points in the constellation.
    '''

    # Set points angles based on the number of points
    angles = np.linspace(0, 2*np.pi, num_points, endpoint=False) + np.pi / 4
    
    # Coordenates of each point in constellation
    coordenates = np.exp(1j * angles)
 
    return coordenates

def gen_symbols(num_symbols, constellation):
    '''
    Returns an array with the complex symbols.

    Parameters
    ----------
    num_symbols : int
        Number of symbols.
    constellation : array
        Array of possible symbol values.
    '''

    # Chooses a random constellation point for each symbol
    symbols = np.random.choice(constellation, num_symbols)

    return symbols

def add_noise(symbols, n_std):
    '''
    Returns the symbol phase after the noise is added.

    Parameters
    ----------
    symbols : array
        Generated symbols.
    n_std : int, float
        Noise standard deviation.
    '''

    num_symbols = symbols.shape[0]

    # List comprehesion to generate an AWGN noise value for each symbol. AWGN noise is a complex gaussian with norm 1.
    noise = np.array([(np.random.normal(0, n_std) + 1j*np.random.normal(0, n_std)) / np.sqrt(2) for n in range(num_symbols)])

    # Add noise to the symbols
    r_symbols = symbols + noise

    return np.exp(1j * np.angle(r_symbols))

def get_channel(ch_std, num_symbols, num_ant):
    '''
    Returns the channel coefficient.

    Parameters
    ----------
    ch_std : int, flot
        Channel standatd deviation.
    num_symbols : int
        Number of symbols.
    num_ant : int
        Number of antennas. 
    '''

    # Channel is a complex gaussian with norm 1
    channel = (np.random.normal(0, ch_std, size=(num_ant, num_symbols)) 
               + 1j*np.random.normal(0, ch_std, size=(num_ant, num_symbols)) / np.sqrt(2))
    
    return channel

def add_channel(symbols, channel, n_std, num_ant):
    '''
    Returns the symbol phase after the channel and noise is added.

    Parameters
    ----------
    symbols : array
        Generated symbols.
    channel : array
        Channel coefficient. 
    ch_std : int, flot
        Channel standatd deviation.
    n_std : int, float
        Noise standard deviation.
    num_ant : int
        Number of antennas.
    '''

    num_symbols = symbols.shape[0]

    # Noise is a complex gaussian with norm 1
    noise = np.array([(np.random.normal(0, n_std) + 1j*np.random.normal(0, n_std)) / np.sqrt(2) for n in range(num_symbols)])

    # Add channel and noise to the symbols
    r_symbols = np.tile(symbols, (num_ant, 1))*channel + noise
    # Returns the received symbols phase
    return np.exp(1j * np.angle(r_symbols))

def mod_compare(constellation, symbols, r_symbols):
    '''
    Maps the received symbols according to the nearest constellation point and returns an boolean array after checking if the transmitted
    phase is egual to received one. 

    Parameters
    ----------
    constellation : array
        Array of possible symbol values.
    symbols : array
        Generated transmitted symbols.
    r_symbols : array
        Received symbols after channel and noise added.
    '''

    num_symbols = symbols.shape[0]

    # Maps the received symbols to the nearest constellation point
    modulation = np.zeros(num_symbols, dtype=np.complex128)

    # Calculate the smaller absolute difference between each symbol and a point in the constellation 
    for s in range(num_symbols):
        modulation[s] = constellation[np.argmin(np.absolute(r_symbols[:, s] - constellation))]

    # Compares the transmitted with the mapped received symbols
    return modulation == symbols    

def symbol_error_rate(modulation):
    '''
    Calculates the SER by dividing the number of False in the array that tells if the received symbol is equal
    to the transmitted one for the total number of symbols.

    Parameters
    ----------
    modulation: array
        array that tells if the received symbol is equal to the transmitted one.
    '''
    return np.count_nonzero(modulation == False) / modulation.shape[0]