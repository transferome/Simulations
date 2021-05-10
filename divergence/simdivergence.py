"""Find the divergence between Gen0, and the Simulation replicates within the
subregion simulation.freqs files, also, change row name to the region"""
import fst.listsimfreqs as lfreqs
import divergence.expdivergence as tools


def region_and_file(freqfile):
    region = freqfile.split('_')[0]
    newfilename = '{}_divergence.freqs'.format(freqfile.split('_simulations.freqs')[0])
    return region, newfilename


def create_dict(freqfile):
    reg, newf = region_and_file(freqfile)
    with open(freqfile) as f:
        data = [line.rstrip('\n').split(',')[1:] for line in f]
        gen0 = tools.float_freqs(data[0])
        gen15 = [tools.float_freqs(sample) for sample in data[1:]]
        
