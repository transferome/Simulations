"""Moves folders for a preselection and founding and ending haplotype frequency data
from the experimental bam files"""
import subprocess
import shutil
import glob
import os
import dirmaker.directorymaker as cdir
import fst.listsimfreqs as lfreqs
import fst.listfst as lfst


def folder_move(source, destination):
    subprocess.call(['mv', source, destination], shell=False)


def output_remove():
    subprocess.call('rm -r *.output', shell=True)


def preselect_move(blueprint):
    maindir = cdir.main_dir(blueprint)
    source_list = list()
    source_list.append(cdir.misc_dir())
    source_list.append(cdir.expfreq_dir())
    source_list.append(cdir.fst_dir())
    for src in source_list:
        folder_move(src, maindir)
    folder_move(maindir, 'results')


def simulation_move(contig, pos1, pos2):
    simdir = cdir.simulation_output_dir()
    freqfiles = lfreqs.zip_freqs()
    fstfilesA = lfst.withinfiles()
    fstfilesB = lfst.withinfiles(replicate='B')
    fstfilesC = lfst.betweenfiles()
    for f1, f2 in freqfiles:
        shutil.move(f1, simdir)
        shutil.move(f2, simdir)
    for a in fstfilesA:
        shutil.move(a, simdir)
    for b in fstfilesB:
        shutil.move(b, simdir)
    for c in fstfilesC:
        shutil.move(c, simdir)
    dest = 'results/{}_{}-{}/'.format(contig, str(pos1), str(pos2))
    folder_move(simdir, dest)
    csvs = glob.glob('*.csv')
    for csv in csvs:
        os.remove(csv)
    datfile = glob.glob('*.dat')[0]
    shutil.move(datfile, dest)
    haplotypesinfo = glob.glob('*.txt')
    hapdir = 'results/{}_{}-{}/haplotype_misc'.format(contig, str(pos1), str(pos2))
    os.mkdir(hapdir)
    for hap in haplotypesinfo:
        shutil.move(hap, hapdir)


if __name__ == '__main__':
    pass
