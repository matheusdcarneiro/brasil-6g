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

    # List comprehesion to generate an AWGN noise value for each symbol
    noise = np.array([np.random.normal(0, n_std) + 1j*np.random.normal(0, n_std) for n in range(num_symbols)])

    # Add noise to the symbols
    r_symbols = symbols + noise

    return r_symbols