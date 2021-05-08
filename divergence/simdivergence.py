"""Find the divergence between Gen0, and the Simulation replicates within the
subregion simulation.freqs files, also, change row name to the region"""
import fst.listsimfreqs as lfreqs


def region_and_file(freqfile):
    region = freqfile.split('_')[0]
    newfilename = '{}_divergence.freqs'.format(freqfile.split('_simulations.freqs')[0])
    return region, newfilename


def create_dict(freqfile):
    with open(freqfile) as f:
        [line.rstrip('\n') for line in freqfile]