"""Functions for cleaning up simulatereads and also organizing lists for the
view, sort, and index command which are needed"""
import glob
import os
import shutil


def listsams(region_tag):
    """Given a region tag from one of the simreadstags, this
    will list all simulatereads created sams for a specific subregion
    in the simulation"""
    return glob.glob('{}-*_simreads.sam'.format(region_tag))


def removesams(region_tag):
    """removes the sam files"""
    sams = listsams(region_tag)
    for sam in sams:
        os.remove(sam)


def listbams(region_tag):
    """Given a region tag from one of the simreadstags, this will
    list all bam files created by samtools view"""
    return glob.glob('{}*simreads*.bam'.format(region_tag))


def movefreqs(region_tag):
    """Lists all the sorted bam files"""
    sorts = glob.glob('{}*simreads*.freqs'.format(region_tag))
    for sort in sorts:
        stem = sort.split('_')[0]
        shutil.move(sort, 'run_{}'.format(stem))
    seeds = glob.glob('{}*simreads.seed'.format(region_tag))
    for seed in seeds:
        stem = seed.split('_')[0]
        shutil.move(seed, 'run_{}'.format(stem))


def removebams(region_tag):
    """removes the list of the original bam files"""
    bams = listbams(region_tag)
    for bam in bams:
        os.remove(bam)


def listall(region_tag):
    return glob.glob('{}*simreads*'.format(region_tag))


if __name__ == '__main__':
    pass
