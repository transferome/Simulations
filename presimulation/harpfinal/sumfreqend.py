"""  Changes sumfreq a bit for the Generation 15 harp runs """
import presimulation.harpinitial.sumfreq as sumf
import glob


class SumFreqEnd(sumf.SumFreq):
    """Sum up files resulting from estimating Generation 15 haplotype frequencies"""

    def __init__(self, chromosome):
        super(SumFreqEnd, self).__init__(chromosome)
        self.chromosome = chromosome
        freqs = glob.glob('*Gen15*.freqs')
        self.freqs = [s for s in freqs if self.chromosome not in s]


if __name__ == '__main__':
    pass
