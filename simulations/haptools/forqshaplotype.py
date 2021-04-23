"""Forqs haplotype object for small windows in forqs"""
# from . import indexgetter as idxgetter
import numpy as np


class ForqsHaplotype:
    """Forqs Haplotype Object
    Example [(0, 91), (1235052, 105), (1251805, 105)]
    or  [(0, 91)]
    """

    def __init__(self, forq_haplotype):
        """Forqs Haplotype Instance Creation"""
        self.info = forq_haplotype
        self.length = len(self.info)
        self.founders = [haplotype_id for position, haplotype_id in self.info]
        self.founders_set = list(set(self.founders))
        self.positions = None
        self.position_map_offset = None
        self.temp_map = None
        self.map = list()

    def haplotype_map_single(self):
        """Create the haplotype guide for assembling the recombined forqs haplotype outputs"""
        if self.length == 1:
            # position_indexes = [idx for idx, position in snp_position_list]
            # # position_values = [position for idx, position in snp_position_list]
            # min_index = min(position_indexes)
            # max_index = max(position_indexes)
            # self.map.append([self.founders_set[0], min_index, max_index])
            self.map.append([self.founders_set[0]])

        else:
            print('Problem making haplotypes from the forqs population file')


def construct_individual(forq_haplotype_object, hap_dict, hap_id_dict):
    """Construct individual using forqs haplotype object and the two dictionaries"""
    # get the value, which is the key for the dgrp hap_dict, from the hap_id_dict
    dgrp_key = hap_id_dict[str(forq_haplotype_object.founders[0])]
    haplotype = hap_dict[dgrp_key]
    # haplotype_seq = haplotype[forq_haplotype_object.map[0][1]:forq_haplotype_object.map[0][2] + 1]
    return haplotype


def process_population(poplist, hap_dict, hap_id_dict):
    """Given the population list from a read in popfile, this constructs haplotypes for all individuals"""
    haplist = list()
    templist = list()
    outlist = list()
    for line in poplist:
        individual = ForqsHaplotype(line)
        individual.haplotype_map_single()
        haplist.append(construct_individual(individual, hap_dict, hap_id_dict))
    for hap in haplist:
        new_hap = list(hap)
        templist.append(new_hap)
    hap_array = np.array(templist)
    hap_trans = hap_array.transpose()
    new_hap_list = hap_trans.tolist()
    for lst in new_hap_list:
        new_line = ','.join(lst)
        outlist.append(new_line)
    return outlist


if __name__ == '__main__':
    pass
