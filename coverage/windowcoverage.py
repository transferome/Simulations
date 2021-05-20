"""Module for Getting Coverage Statistics and Plots from a Coverage File"""
# from . import resource_dir
import subprocess
from multiprocessing import Pool
import glob
import harpsnp.filedict as xfiles
import dirmaker.directorymaker as cdir
# import coverage.listcovfiles as listcoveragefiles


def get_windows(contig, pos1, pos2):
    blue_print_file = 'results/{}_{}-{}/{}-{}_blueprint.txt'.format(contig, str(pos1), str(pos2), str(pos1), str(pos2))
    windows = [line.split(',')[0] for line in open(blue_print_file)]
    return windows


def snp_positions(contig, blue_print_window):
    dgrp_pos = [int(line.split(',')[0]) for line in open(xfiles.snps[contig]) if not line.startswith(contig)]
    # the window will be a list of length two
    window_list = blue_print_window.lstrip('{}:'.format(contig)).split('-')
    # not including SNP at end of window because it is start of next window
    dgrp_pos_in_window = [x for x in dgrp_pos if int(window_list[0]) <= x < int(window_list[1])]
    return window_list, dgrp_pos_in_window


def bed_file(contig, pos1, pos2, window_list, dgrp_pos_in_window):
    covdir = cdir.coverage_dir(contig, pos1, pos2)
    bedfile = f"{covdir}/{contig}_{window_list[0]}-{window_list[1]}.bed"
    with open(bedfile, "w+") as bf:
        for pos in dgrp_pos_in_window:
            bf.write(f"{contig}\t{pos}\t{pos + 1}\t{pos}_SNP\n")
    return bedfile


def make_beds(contig, pos1, pos2):
    wins = get_windows(contig, pos1, pos2)
    bed_files_windows_list = list()
    for win in wins:
        win_list, dgrp_pos = snp_positions(contig, win)
        b_file = bed_file(contig, pos1, pos2, win_list, dgrp_pos)
        bed_files_windows_list.append(b_file)
    return zip([contig] * len(wins), wins, bed_files_windows_list)


def list_experimental_bams():
    return glob.glob('harpsnp/resources/*.bam')


def samtools_depth_commands(bed_files_window_tuple_list):
    command_list = []
    bam_files = list_experimental_bams()
    for bam in bam_files:
        for contig, win, bedf in bed_files_window_tuple_list:
            bed_path = '/'.join(bedf.split('/')[:-1])
            bam_sample = bam.split('/')[-1].split('_')[0]
            output_file = f"{bed_path}/{bam_sample}_{contig}_{win[0]}-{win[1]}.coverage"
            command = f'samtools depth -a {bam} -b {bedf} > {output_file}'
            command_list.append(command)
    return command_list
    # subprocess.call(command, shell=True)


def samtools_depth(command_input):
    subprocess.call(command_input, shell=True)


def samtools_depth_multi(bed_files_window_tuple_list):
     pool = Pool(18)
     commands = samtools_depth_commands(bed_files_window_tuple_list)
     pool.map(samtools_depth, commands)


if __name__ == '__main__':
    pass
    # cont = '2L'
    # posa = 500000
    # posb = 23093611
    # # # dgrp_coverage_files(cont, posa, posb)
    # win = get_windows(cont, posa, posb)
    # ps = snp_positions(cont, win[0])
