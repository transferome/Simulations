"""Class object for handling creation of haplotypes for simulatereads, and a function
which returns a list of the objects"""
import os
import simulations.haptools.samplehaplotypedict as id_dict


class ConstructorTag:
    """Takes a subtag from a TagForqs object and creates a specific tag for
    the population.txt file from forqs which is used to create a haplotype file
    for simulatereads to process"""

    def __init__(self, forqstag_obj, forqs_subtag, replicate):
        """Initialize and process tag"""
        self.tag = forqs_subtag
        self.contig = forqstag_obj.contig
        self.region = forqstag_obj.region
        self.region_length = forqstag_obj.region_length
        self.replicate = replicate
        self.recombination_file = forqstag_obj.recombination_file
        self.population_file = 'run_{}/population_final_pop1.txt'.format(forqs_subtag)
        self.output_snpfile = 'run_{}/{}_haplotypes.txt'.format(forqs_subtag, forqs_subtag)
        self.config_file = '{}/run_{}/{}_simreads.config'.format(os.getcwd(), forqs_subtag, forqs_subtag)
        self.sample_file = '{}-{}_rep{}.sample'.format(self.region[0], self.region[1], replicate)
        self.haplotype_frequencies = None
        with open(self.sample_file) as sfile:
            for line in sfile:
                if line.startswith(self.tag):
                    self.haplotype_frequencies = line.rstrip('\n').split(',')[1:]
            if self.haplotype_frequencies is None:
                print('Cant get haplotype frequencies from sample file')
                quit()
        # print(self.haplotype_frequencies)
        self.haplotype_id_dict = id_dict.make_id_map(self.haplotype_frequencies)
        self.duplicate_haplotype_number = None


def construct_taglist(forqstag_obj, replicate):
    """Return list of tags for processing"""
    tag_list = list()
    for tag in forqstag_obj.subtags:
        tag_list.append(ConstructorTag(forqstag_obj, tag, replicate))
    return tag_list


def list_simreadsconifgs(constructor_tags):
    """Lists all of the simulatereads configs"""
    config_list = list()
    for tag in constructor_tags:
        config_list.append(tag.config_file)
    return config_list


if __name__ == '__main__':
    pass
