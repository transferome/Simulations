"""Moves folders for a preselection and founding and ending haplotype frequency data
from the experimental bam files"""
import subprocess
import dirmaker.directorymaker as cdir


def folder_move(source, destination):
    subprocess.call(['mv', source, destination], shell=False)


def preselect_move(blueprint):
    maindir = cdir.main_dir(blueprint)
    source_list = list()
    source_list.append(cdir.misc_dir())
    source_list.append(cdir.expfreq_dir())
    source_list.append(cdir.fst_dir())
    for src in source_list:
        folder_move(src, maindir)
    folder_move(maindir, 'results')


if __name__ == '__main__':
    pass
