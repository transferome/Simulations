"""Module for Getting Coverage Statistics and Plots from a Coverage File"""
import harpsnp.filedict as xfiles
import dirmaker.directorymaker as cdir
import coverage.listcovfiles as listcoveragefiles


def get_windows(contig, pos1, pos2):
    blue_print_file = 'results/{}_{}-{}/{}-{}_blueprint.txt'.format(contig, str(pos1), str(pos2), str(pos1), str(pos2))
    windows = [line.split(',')[0] for line in open(blue_print_file)]
    return windows


def snp_positions(contig, blue_print_window):
    dgrp_pos = [int(line.split(',')[0]) for line in open(xfiles.snps[contig]) if not line.startswith(contig)]
    # the window will be a list of length two
    window_list = blue_print_window.lstrip('{}:'.format(contig)).split('-')
    dgrp_pos_in_window = [x for x in dgrp_pos if int(window_list[0]) <= x <= int(window_list[1])]
    return window_list, dgrp_pos_in_window


def snp_depths(contig, positions_in_window, coverage_file):
    window_coverage_list = list()
    with open(coverage_file) as covf:
        for line in covf:
            if line.startswith(contig):
                current_position = int(line.split('\t')[1])
                if current_position in positions_in_window:
                    window_coverage_list.append(line)
    return window_coverage_list


def create_window_depth_files(contig, blue_print_window, coverage_file, coverage_directory):
    sample = coverage_file.split('_')[0].split('/')[-1]
    window, snp_pos = snp_positions(contig, blue_print_window)
    snp_cov = snp_depths(contig, snp_pos, coverage_file)
    output_name = '{}/{}-{}_{}.coverage'.format(coverage_directory, window[0], window[1], sample)
    with open(output_name, 'w+') as outputfile:
        for outline in snp_cov:
            outputfile.write(outline)


def dgrp_coverage_files(contig, pos1, pos2):
    windows = get_windows(contig, pos1, pos2)
    cov_dir = cdir.coverage_dir(contig, pos1, pos2)
    cov_files = listcoveragefiles.listcov()
    for cov_file in cov_files:
        for window in windows:
            create_window_depth_files(contig, window, cov_file, cov_dir)


if __name__ == '__main__':
    pass
    # os.chdir('C://Users//ltjon/Data//Mel2018_Experimental_Haplotype_Graphs')
    # begin = time.time()
    # cont = '2R'
    # posa = 4200000
    # posb = 25258235
    # main(cont, posa, posb)
    # end = time.time()
    # print(end - begin)
