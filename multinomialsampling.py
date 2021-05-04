"""Take the results of Generation 0 frequency estimates, and create a multinomial
sample of haplotypes (individuals) from the DGRP in the regions"""
import multinomialfreqs.foundinghaplotypesampling as sampler
import simulations.processtags as mainsim
import simulations.subregionprocess as subsim
import simulations.simfst.fstsimulate as fst


def main(contig, pos1, pos2, simulation_pairnumber):
    sampler.starting_frequencies(contig, pos1, pos2, simulation_pairnumber)
    simtags_a = mainsim.make_tags(contig, simulation_pairnumber * 2, replicate='A')
    subsim.subregion_processes(simtags_a, pos1, pos2, replicate='A')
    simtags_b = mainsim.make_tags(contig, simulation_pairnumber * 2, replicate='B')
    subsim.subregion_processes(simtags_b, pos1, pos2, replicate='B')


def sim_fst(contig, pos1, pos2):
    fst.fst_betweenreplicate()
    fst.average_fst(contig, pos1, pos2)


if __name__ == '__main__':
    # import argparse
    # parser = argparse.ArgumentParser(description="Presimulation: Estimation Windows Program")
    # parser.add_argument("-c", "--chr", help='chromosome')
    # parser.add_argument("-b", '--begin', help='first position')
    # parser.add_argument("-e", '--end', help='end position')
    # parser.add_argument('-n', '--number', help='number of recombination simulations')
    # args = parser.parse_args()
    cont = '2L'
    main(cont, 4000000, 20000000, 100)
    sim_fst(cont, 4000000, 20000000)
