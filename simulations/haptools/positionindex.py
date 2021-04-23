"""Creates list of positions and their index"""


def position_index(constructor_tag):
    """Gets list of positions, and indexes them with enumerate"""
    range_file = 'dgrp{}_rangesubset.txt'.format(constructor_tag.contig)
    # pos_list = list()
    # subtractor is used to adjust the SNP positions from simulations that don't start at 0
    # for example 1,000,000 to 2,000,000 range has first SNP as 1005816
    # but in the forqs population file, 1,005,816 does not exist, from the start of the simulated chromosome
    # that actually exists at 5816 in forqs positions, so have to subtract 1,000,000
    subtractor = constructor_tag.region[0]
    with open(range_file) as f:
        pos_list = [int(line.split('\t', 1)[0]) - subtractor for line in f]
        # for line in f:
        #     pos = int(line.split('\t')[0]) - subtractor
        #     pos_list.append(pos)
    return list(enumerate(pos_list))


if __name__ == '__main__':
    pass
