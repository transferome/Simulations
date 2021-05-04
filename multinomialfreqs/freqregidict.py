"""Make a dictionary for the two replicates into an object,
the region will be the key, and the values will be the frequencies of the DGRP haplotypes
at that region"""
from . import drawhaplotypes as dp


class FreqDict:
    """Dictionary of estimated harp frequencies at region intervals"""

    def __init__(self, contig, pos1, pos2):
        self.repAfile = 'results/{}_{}-{}/replicateA_frequencies.txt'.format(contig, pos1, pos2)
        self.repBfile = 'results/{}_{}-{}/replicateB_frequencies.txt'.format(contig, pos1, pos2)
        self.A = {line.split(',')[0]: line.rstrip('\n').split(',')[1:] for line in open(self.repAfile)}
        self.B = {line.split(',')[0]: line.rstrip('\n').split(',')[1:] for line in open(self.repBfile)}


class SamplingDict:
    """Creates the dictionary that is the """

    def __init__(self, freqdict_dict, rdaw):
        self.dictionary = dp.random_dict(freqdict_dict, rdaw)

    def write_samples(self, replicate='A'):
        """Write the dictionary information to a file"""
        for idx, key in enumerate(self.dictionary.keys(), 1):
            sampling_array = self.dictionary[key]
            # sampling_list = sampling_array.tolist()
            with open('{}_rep{}.sample'.format(key, replicate), 'w+') as f:
                for idy, lst in enumerate(sampling_array, 1):
                    f.write("r{}-m{}u,{}\n".format(str(idx), str(idy), ','.join([str(x) for x in lst])))
                    f.write("r{}-m{}d,{}\n".format(str(idx), str(idy), ','.join([str(x) for x in lst])))


if __name__ == '__main__':
    pass
