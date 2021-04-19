"""Need a module to list the simulation.freq files created by the simreads simulations.
I also need to pair those files together, region 8291027-8388036 has two files, a repA and a repB.
Each line of the paired files gets compared using fst"""
import glob


def zip_freqs():
    """Lists both the rep A and rep B simulation.freqs files"""
    freqsA = glob.glob('*RepA_simulations.freqs')
    freqsB = glob.glob('*RepB_simulations.freqs')
    freqsA.sort(key=lambda x: int(x.split('-')[0]))
    freqsB.sort(key=lambda x: int(x.split('-')[0]))
    return zip(freqsA, freqsB)


if __name__ == '__main__':
    pass
