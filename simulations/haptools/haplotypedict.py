"""Create haplotype dictionary using the mixed tranpose file created by the organize
module"""


def haplodict(constructor_tag):
    """Takes the transposed dataframe and creates a dictionary, where key is DGRP# and value
    is the haplotype sequence"""
    transpose_filename = 'dgrp{}_mixed_transpose.txt'.format(constructor_tag.contig)
    data = [line.rstrip('\n') for line in open(transpose_filename)]
    data_dict = {str(line.split('\t', 1)[0]): line.split('\t', 1)[1].replace('\t', '') for line in data}
    del data_dict['position']
    return data_dict


if __name__ == '__main__':
    pass
