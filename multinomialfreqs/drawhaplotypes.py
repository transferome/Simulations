"""Draws a multinomial sample of the dgrp haplotypes given a list of the estimated
frequencies of the dgrp at a region.  It returns a numpy array, which is essentially
a list, of lists, which contain a sequence of numbers, the length of the number of dgrp lines
and in the same order of the frequencies, so this directly maps with how many of each DGRP line is
drawn.  [3, 4, 68...]  means 3 of line_21, 4 of line_ etc..."""
import numpy as np


def random_draw(frequency_list, individuals_drawn, number_of_random_draws):
    """Given a frequency_list this returns a numpy array, with
    vectors the length of the number of haplotypes"""
    xfreqs = [float(x) for x in frequency_list]
    xnorm = [x/sum(xfreqs) for x in xfreqs]
    return np.random.multinomial(individuals_drawn, xnorm, number_of_random_draws)


def random_dict(region_frequency_dictionary, number_of_random_draws):
    """using the region and frequency dictionary, this creates a dictionary
    of multinomial samplings of the dgrp haplotypes, given a number of individuals, which I'm currently
    making static here at 500"""
    indi_draw = 500
    outdict = dict()
    for key in region_frequency_dictionary.keys():
        frequencies = region_frequency_dictionary[key]
        sampling_array = random_draw(frequencies, indi_draw, number_of_random_draws)
        outdict[key] = sampling_array
    return outdict


if __name__ == '__main__':
    pass
