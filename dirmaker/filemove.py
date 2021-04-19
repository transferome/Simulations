"""Moves files out of main directory and into a subfolder when needed"""
import glob
import shutil
import dirmaker.directorymaker as cdir
import subprocess


def gen0freq():
    gen0files = glob.glob('*_Gen0*.freqs')
    gen0files = [s for s in gen0files if 'combined' not in s]
    dest = cdir.expfreq_dir()
    for file in gen0files:
        shutil.move(file, dest)


def expfst():
    expfiles = glob.glob('Exp*_Fst.dat')
    fstdir = cdir.fst_dir()
    for file in expfiles:
        shutil.move(file, fstdir)


def endfrqtxt():
    endfiles = glob.glob('end*_frequencies.txt')
    mscdir = cdir.misc_dir()
    for file in endfiles:
        shutil.move(file, mscdir)


def combinemove(bloop, combined_files):
    hapdir = cdir.exp_haplotype_estimate_dir()
    for file in combined_files:
        shutil.move(file, hapdir)
    maindir = cdir.main_dir(bloop)
    subprocess.call(['mv', hapdir, '{}/'.format(maindir)], shell=False)


def simfilesmove(bloop):
    maindir = cdir.main_dir(bloop)
    repfreqs = glob.glob('replicate*_frequencies.txt')
    bluefile = glob.glob('*_blueprint.txt')
    for freq in repfreqs:
        shutil.move(freq, maindir)
    for blue in bluefile:
        shutil.move(blue, maindir)


if __name__ == '__main__':
    pass
