"""Generate haplotypes from the forqs population files"""
import simulations.haptools.haplotypedict as hdict
# import haptools.positionindex as posidx
import simulations.haptools.readpopfile as popread
import simulations.haptools.forqshaplotype as constructor
import simulations.haptools.writesnptable as writer
# import duplicatefinder.listduplicatecounter as duplicates


def generate(constructor_tag):
    """Makes haplotypes"""
    ref_file = 'dgrp{}_subset.txt'.format(constructor_tag.contig)
    # pos_id_list = posidx.position_index(constructor_tag)
    hap_dict = hdict.haplodict(constructor_tag)
    pop_file = popread.readpop(constructor_tag.population_file)
    output_haplotypes = constructor.process_population(pop_file, hap_dict, constructor_tag.haplotype_id_dict)
    # constructor_tag.duplicate_haplotype_number = duplicates.duplicate_counter(output_haplotypes)
    # print(output_haplotypes)
    writer.write_snp_table(ref_file, output_haplotypes, constructor_tag)
    # print(constructor_tag.duplicate_haplotype_number)


if __name__ == '__main__':
    pass
