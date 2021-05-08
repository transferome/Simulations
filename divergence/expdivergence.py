"""Calculates the difference between the Generation 0 frequency estimates, and the
Generation 15 frequency estimates"""
import dirmaker.directorymaker as cdir
import glob
import numpy as np


def open_file(freqfile):
    with open(freqfile) as input_file:
        datadict = {int(line.split(',')[0]): line.rstrip('\n').split(',')[1:] for line in input_file}
    return datadict


def float_freqs(freqlist):
    return [float(s) for s in freqlist]


def subtract_vectors(gen15vec, gen0vec):
    return list(np.subtract(np.array(gen15vec), np.array(gen0vec)))


def define_genzero(cont, pos1, pos2, replicate='A'):
    pardir = cdir.results_experimental_dir(cont, pos1, pos2)
    if replicate == 'A':
        outdat = open_file('{}/Gen0A_combined.freqs'.format(pardir))
        return outdat
    else:
        outdat = open_file('{}/Gen0B_combined.freqs'.format(pardir))
        return outdat


def list_genfifteen(cont, pos1, pos2, replicate='A'):
    pardir = cdir.results_experimental_dir(cont, pos1, pos2)
    if replicate == 'A':
        return glob.glob('{}/Gen15*A*.freqs'.format(pardir))
    else:
        return glob.glob('{}/Gen15*B*.freqs'.format(pardir))


def name_change(freqfile):
    return '{}divergence.freqs'.format(freqfile.split('combined.freqs')[0])


def write_divergence(cont, pos1, pos2):
    for i in ['A', 'B']:
        gen15_files = list_genfifteen(cont, pos1, pos2, replicate=i)
        gen0a = define_genzero(cont, pos1, pos2, replicate=i)
        for file in gen15_files:
            newname = name_change(file)
            gen15 = open_file(file)
            with open(newname, 'w+') as outf:
                key_list = list(gen0a.keys())
                key_list.sort()
                for key in key_list:
                    vec15_temp = gen15[key]
                    vec15 = float_freqs(vec15_temp)
                    vec0_temp = gen0a[key]
                    vec0 = float_freqs(vec0_temp)
                    diverge = subtract_vectors(vec15, vec0)
                    diverge_string = '{},{}\n'.format(key, ','.join([str(round(x, 8)) for x in diverge]))
                    outf.write(diverge_string)


if __name__ == '__main__':
    pass
