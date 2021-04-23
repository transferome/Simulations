"""Creates a tag object class, and also a class object that holds all of
the various sample files that will be used to run simulations"""
import glob


class RegionSampleTag:
    """Give each sub simulation a tag of information"""
    numInstances = 0

    def __init__(self, filename, contig, simulation_number, replicate):
        """Attach info to object"""
        RegionSampleTag.numInstances = RegionSampleTag.numInstances + 1
        self.filename = filename
        temp_reg = filename.split('_')[0]
        self.region = int(temp_reg.split('-')[0]), int(temp_reg.split('-')[1])
        self.region_length = len(range(self.region[0], self.region[1] + 1))
        self.directory = '{}-{}_{}'.format(temp_reg, filename.split('.')[0].split('_')[1], replicate)
        self.region_sample_tags = [line.split(',')[0] for line in open(filename)]
        self.contig = contig
        self.simulation_number = simulation_number
        self.replicate = replicate
        self.recombination_file = 'dmel_recRates_{}_{}-{}.csv'.format(contig, self.region[0], self.region[1])

    @staticmethod
    def regiontag_number():
        print("Created {}  Region Tags".format(RegionSampleTag.numInstances))


class TagMaker:
    """A list of all of the """

    def __init__(self, contig, simulation_number):
        """Gather files"""
        self.repA = glob.glob('*repA.sample')
        self.repB = glob.glob('*repB.sample')
        self.tags = list()
        self.contig = contig
        self.simulation_number = simulation_number

    def create(self, replicate='A'):
        """Create tags and add them to lists"""
        if replicate == 'A':
            for file in self.repA:
                self.tags.append(RegionSampleTag(file, self.contig, self.simulation_number, replicate))
        else:
            for file in self.repB:
                self.tags.append(RegionSampleTag(file, self.contig, self.simulation_number, replicate))


if __name__ == '__main__':
    pass
