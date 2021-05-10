"""Find the divergence between Gen0, and the Simulation replicates within the
subregion simulation.freqs files, also, change row name to the region"""
import os
import fst.listsimfreqs as lfreqs
import divergence.expdivergence as tools


def region_and_file(freqfile):
    region = freqfile.split('_')[0]
    newfilename = '{}_divergence.freqs'.format(freqfile.split('_simulations.freqs')[0])
    return region, newfilename


def create_file(freqfile):
    reg, newf = region_and_file(freqfile)
    diverged_data = list()
    with open(freqfile) as f:
        data = [line.rstrip('\n').split(',')[1:] for line in f]
        gen0 = tools.float_freqs(data[0])
        gen15 = [tools.float_freqs(sample) for sample in data[1:]]
        for g in gen15:
            diverged_data.append(tools.subtract_vectors(g, gen0))
    with open(newf, 'w+') as outf:
        for line in diverged_data:
           outf.write('{},{}\n'.format(reg, ','.join([str(round(x, 8)) for x in line])))


def simdiverge(cont, pos1, pos2):
    os.chdir('results/{}_{}-{}/Sim_Frequencies_Fst'.format(cont, pos1, pos2))
    zipf = lfreqs.zip_freqs()
    for fa, fb in zipf:
        create_file(fa)
        create_file(fb)


if __name__ == '__main__':
    pass
