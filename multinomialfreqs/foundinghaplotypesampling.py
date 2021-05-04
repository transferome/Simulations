"""Uses multinomial sampling to sample haplotypes given the starting frequencies
estimated from harp.  This samples 2000 haplotypes, which is thus equivalent
to 1000 diploid individuals.  For each subregion, it creates a specified number of
  multinomial draws, into a sample file.  The currently value of 20 for example.
  Creates a file of 20 lines in length for each subregion, with a different multinomial
  draw from the starting estimate frequencies.  The 20 value can be altered as desired
  at this point, it is arbitrary"""
# import core.timetracer as timer
import multinomialfreqs.freqregidict as fdict


# @timer.timer(label='Frequencies')
def starting_frequencies(contig, pos1, pos2, simulation_pairs):
    frequency_dictionary = fdict.FreqDict(contig, pos1, pos2)
    # currently sampling 20 multinomial frequency distributions
    sample_a = fdict.SamplingDict(frequency_dictionary.A, simulation_pairs)
    sample_a.write_samples(replicate='A')
    sample_b = fdict.SamplingDict(frequency_dictionary.B, simulation_pairs)
    sample_b.write_samples(replicate='B')


if __name__ == '__main__':
    pass
