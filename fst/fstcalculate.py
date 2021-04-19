"""Calculates Fst given two strings of frequency"""


def pooled_expected_heterozygosity(frequency_list1, frequency_list2):
    """This function calculates expected heterozygosity by first finding the mean frequency of each
    haplotype(allele), and then by subtracting 1 from the sum of squares of those values.
    This is the expected heterozygosity if these two poulations were one population"""
    pbar_list = list()
    for x, y in zip(frequency_list1, frequency_list2):
        pbar = (float(x) + float(y))/2
        pbar_list.append(pbar)
    return 1 - sum([float(s)**2 for s in pbar_list])


def heterozygosity(sample_frequency_list):
    """Returns expected heterozygosity for a population sample given a normalized list of frequencies
    The heterozygosity function will normalize most of the harp frequency vectors, they generally do not sum
    exactly to 1, but very very close.  Adjustment probably doesn't matter, only a precaution."""
    frequency_sum = sum([float(s) for s in sample_frequency_list])
    if frequency_sum == 1:
        return 1 - sum([float(s)**2 for s in sample_frequency_list])
    else:
        # print(str(frequency_sum))
        normed = [float(s)/frequency_sum for s in sample_frequency_list]
        return 1 - sum([float(s)**2 for s in normed])


def average_expected_heterozygosity(frequency_list1, frequency_list2):
    """This function calculates observed heterozygosity by taking the average of the
    observed heterozygosity in the two subpopulations"""
    h1 = heterozygosity(frequency_list1)
    h2 = heterozygosity(frequency_list2)
    return (h1+h2)/2


def fst(frequency_list1, frequency_list2):
    """This function calculates Fst using the observed and expected heterozygosity functions.
    Fst = (Ht - Hs)/Ht   That reduces to 1 - Hs/Ht
     Remember Fst 0 means variation is not explained by differences in the populations, 1 means that the
     variation is due to differences in populations"""
    ht = pooled_expected_heterozygosity(frequency_list1, frequency_list2)
    hs = average_expected_heterozygosity(frequency_list1, frequency_list2)
    return 1 - (hs/ht)


if __name__ == '__main__':
    pass
