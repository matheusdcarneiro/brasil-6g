import numpy as np

def selection_combiner(r_symbols, channel):

    w_symbols = channel.conj() * r_symbols

    combined_symbols = np.zeros((1, channel.shape[1]), dtype=np.complex128)

    for s in range(channel.shape[1]):

        combined_symbols[:, s] = np.max(w_symbols[:, s])

    return combined_symbols
    