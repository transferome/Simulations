"""Creates the Blue Print For How to Estimate Haplotype Frequencies Mainly
Using the simparam object"""
import harpsnp.snp_count as scount


def walk_region(starting_region, no_recombination_length):
    """Make multiple tuples, verifying that the window size is appropriate over entire starting range"""
    starts = list(range(starting_region[0], starting_region[1], no_recombination_length))
    ends = starts[1:] + [starting_region[1]]
    valid_regions = list(zip(starts, ends))
    return valid_regions[:-1]


class ParamBlueprint:
    """Using the Sim Param Class, this captures the chromosomal regions used to
    estimate the haplotype frequencies in the experimental sequence data, and the
    parameter info from the PreSimParam class to describe how the the regions were
    estimated, and the snp density within the resulting chromosomal regions"""

    def __init__(self, chromosome, window, simulation_number, param_obj):
        self.chromosome = chromosome
        self.window = window
        self.simulation_number = simulation_number
        self.SimParam = param_obj
        self.region_size = None
        self.windows = None
        self.recombination_array = None
        self.length_array = None
        self.file = None

    def make(self):
        """Testing recombination along length of whole region"""
        simulator = self.SimParam(self.chromosome, self.window, self.simulation_number)
        simulator.test_recombination()
        self.windows = walk_region(self.window, simulator.region_length)
        self.region_size = simulator.region_length
        recombination_array = list()
        length_array = list()
        for item in self.windows:
            simulator = self.SimParam(self.chromosome, item, self.simulation_number)
            simulator.try_recombination()
            recombination_array.append(simulator.recombination_number)
            length_array.append(simulator.region_length)
        self.length_array = length_array
        self.recombination_array = recombination_array

    def write(self, original_window):
        """Write information gathered by the simulation and the simulation blueprint,
        to create a file which can be used to execute harp, and record information
        about the regions to be simulated"""
        self.file = '{}_blueprint.txt'.format('-'.join([str(x) for x in original_window]))
        with open(self.file, 'w+') as outfile:
            for j, k, l in zip(self.windows, self.recombination_array,
                               self.length_array):
                snp_number = scount.count_snps(self.chromosome, j)
                original_region = '-'.join([str(x) for x in original_window])
                location = '{}:{}'.format(self.chromosome, '-'.join([str(x) for x in j]))
                outfile.write('{}\n'.format(','.join([location, original_region,
                                                      str(k), str(l), str(snp_number),
                                                      str(self.simulation_number)])))


if __name__ == '__main__':
    pass
