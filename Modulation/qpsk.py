import numpy as np
def random_symbol():

    constelation = [np.pi/4, 3 * np.pi/4, 5 * np.pi/4, 7 * np.pi/4]

    phase = np.random.choice(constelation)


    xs = 0

    xc = 0

    if np.sin(phase) > 0:

        xs = 1

    else:

        xs = 0

    if np.cos(phase) > 0:

    
        xc = 1

    else: 

        xc = 0

    print(complex(xs, xc))

    return np.exp(1j * phase)



def symbol_receptor(symbol_):

    real_part = np.real(symbol_)

    module = np.abs(symbol_)

    added_phase = np.arccos(real_part / module)

    quadrature = np.sin(added_phase)

    in_phase = np.cos(added_phase)

    xs = 0

    xc = 0

    if quadrature > 0:

        xs = 1

    else:

        xs = 0

    if in_phase > 0:


        xc = 1

    else: 

        xc = 0

    return complex(xs, xc)


def db2lin(x):

    return 10 * np.log10(x)


def main():

    symbol = random_symbol()



    snr = 5 # db 

    noise_power = 1 / db2lin(snr)

    noise_sigma = np.sqrt(noise_power)

    noise_signal = np.random.normal(0,noise_sigma)/np.sqrt(2) + 1j * np.random.normal(0,noise_sigma)/np.sqrt(2)

    received_signal = symbol + noise_signal

    recebido = symbol_receptor(received_signal)

    print(recebido)


main()