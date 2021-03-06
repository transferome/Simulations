"""Converts rcc map from webform to type used by preforqs"""
from . import resources_dir
import numpy as np


def read_rcc(filename):
    """Reads in rcc text"""
    with open(filename) as f:
        out_list = list()
        for line in f:
            line = line.replace(' ', '')
            line = line.rstrip('\n')
            out_list.append(line)
    return out_list


def subset_rcc(rcc_list, chr_arm, chromosome_range):
    """Subset the rcc text list"""
    out_list = list()
    newfile = '{}_{}-{}.csv'.format(chr_arm, chromosome_range[0], chromosome_range[1])
    with open(newfile, 'w+') as f:
        for line in rcc_list[1:]:
            if int(chromosome_range[0]) <= int(line.split('\t')[0].split('..')[0].split(':')[-1]) < int(chromosome_range[1]):
                out_list.append(line)
                f.write(line)
    return out_list


def get_midpoint(data, lower_bound):
    """Get midpoint value for each row"""
    out_list = list()
    for line in data[1:]:
        mid_point = (int(line.split('\t')[0].split('..')[-1]) + int(line.split('\t')[0].split('..')[0].split(':')[-1]))//2
        # TODO: is subtracting chromosome length from mid-point really what I want to fix range problem
        mid_point = mid_point - int(lower_bound)
        out_list.append(str(mid_point))
    return out_list


def get_midpoint_rate(data):
    """Gets the cameron midpoint rate"""
    out_list = list()
    for line in data:
        value = float(line.split('\t')[5])
        out_list.append(value)
    return out_list


def get_cumulative_rate(mid_rate_list):
    """Gets cumulate rate from midpoint_rate list"""
    mid_list = [x/10 for x in mid_rate_list]
    cum_array = np.cumsum(mid_list)
    out_list = cum_array.tolist()
    return [round(x, 5) for x in out_list]


def write_recmap(pos, mid, cum, chr_arm, chromosome_range):
    """Writes information to new file"""
    newfilename = 'dmel_recRates_{}_{}-{}.csv'.format(chr_arm, chromosome_range[0], chromosome_range[1])
    header = "position COMBINED_rate(cM / Mb) Genetic_Map(cM)\n"
    mid_str = [str(x) for x in mid]
    cum_str = [str(x) for x in cum]
    with open(newfilename, 'w+') as f:
        f.write(header)
        f.write("50000 0 0\n")
        for p, m, c in zip(pos, mid_str, cum_str):
            line = '{}\n'.format(' '.join([p, m, c]))
            f.write(line)
    return newfilename


def main_recmap(chromosome_range, chr_arm='2R'):
    """Main functions combines previously defined functions into one function"""
    chr_list = ['2R', '2L', '3L', '3R']
    if chr_arm in chr_list:
        filename = '{}/{}rcc.txt'.format(resources_dir, chr_arm)
        rcc_file = read_rcc(filename)
        dat = subset_rcc(rcc_file, chr_arm, chromosome_range)
        positions = get_midpoint(dat, chromosome_range[0])
        mid_rate = get_midpoint_rate(dat)
        cum_rate = get_cumulative_rate(mid_rate)
        new_recmap = write_recmap(positions, mid_rate, cum_rate, chr_arm, chromosome_range)
        return new_recmap
    else:
        print('No Valid rcc File Given')


def print_filename(chr_arm):
    """Print the filename of the file"""
    filename = '{}/{}rcc.txt'.format(resources_dir, chr_arm)
    print(filename)


if __name__ == '__main__':
    pass
    # test = main_recmap([2000000, 4000000], '3L')
