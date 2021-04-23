"""Create config for simulating selection, starting from """
from . import resource_file
from presimulation.recombination import convert_recmap as converter
from presimulation.forqsprep.config import list_simulation_configs


class TagConfigs:
    """Make forqs configs for the simulations, and tag them using the tag object"""

    def __init__(self, simulation_tag):
        """instance start"""
        self.tag = simulation_tag
        self.directory = simulation_tag.directory
        self.contig = simulation_tag.contig
        self.region = simulation_tag.region
        self.region_length = simulation_tag.region_length
        self.recombination_file = simulation_tag.recombination_file
        self.subtags = simulation_tag.region_sample_tags
        self.simulation_number = simulation_tag.simulation_number
        self.config_list = None

    def create_configs(self):
        """Create a config file for a multinomial sampled region"""
        converter.main_recmap(self.region, chr_arm=self.contig)
        for s in self.subtags:
            with open(resource_file) as infile, open('run_{}.config'.format(s), 'w+') as outfile:
                for line in infile:
                    if 'chromosome_lengths' in line:
                        new_line = line.replace('2799800', str(self.region_length))
                        outfile.write(new_line)
                    # elif line.endswith('.csv\n'):
                    #     new_line = line.replace('dmel_recRates_3L_5100200-7900000.csv', self.recombination_file)
                    #     outfile.write(new_line)
                    elif 'output_directory' in line:
                        new_line = line.replace('chr3L_0', 'run_{}'.format(s))
                        outfile.write(new_line)
                    else:
                        outfile.write(line)

    def list_configs(self):
        """List created config files"""
        self.config_list = list_simulation_configs()


if __name__ == '__main__':
    pass
