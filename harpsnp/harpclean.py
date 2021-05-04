"""Remove outputs produced by Harp"""
import glob
import shutil
import os
import dirmaker.directorymaker as cdir


def remover(outdirs):
    """removes the output directories, and hlk_files"""
    hlks = glob.glob('*.hlk')
    for direct in outdirs:
        shutil.rmtree(direct)
    for file in hlks:
        os.remove(file)


def bamremover():
    bam_files = glob.glob('*.bam*')
    for file in bam_files:
        os.remove(file)


def move_freq():
    endir = cdir.expfreq_dir()
    freqs = glob.glob('*Gen15*.freqs')
    for freq in freqs:
        shutil.move(freq, endir)


class InitialClean:
    """Clean results of harp at Generation 0"""

    def __init__(self):
        output_directories = glob.glob('*Master.output')
        remover(output_directories)


class HarpEndClean:
    """Clean results of harp at Generation 15"""

    def __init__(self, blueprint):
        output_directories = glob.glob('*Gen15*.output')
        remover(output_directories)
        move_freq()


class SimClean(InitialClean):
    """Cleans the results of the simulations"""
    def __init__(self):
        super(SimClean, self).__init__()
        bamremover()


if __name__ == '__main__':
    pass
