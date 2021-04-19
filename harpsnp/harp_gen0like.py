"""Multiprocessing of harp like command"""
import subprocess
from multiprocessing import Pool
from functools import partial
# from . import resources
from harpsnp import filedict as xfiles
import psutil
import os


def limit_cpu():
    """Called At Every Process Started in a multiprcoess pool"""
    p = psutil.Process(os.getpid())
    p.nice(3)


def like_process(chromosome, region, bam):
    """Execute harp like command and process"""
    # ref file is always the same
    if 'S21' in bam:
        stem = '{}_Gen0RepAMaster'.format(region)
    else:
        stem = '{}_Gen0RepBMaster'.format(region)
    subprocess.call(['harp', 'like', '--bam', bam, '--region', region, '--refseq', xfiles.reference, '--snps',
                     xfiles.snps[chromosome], '--stem', stem], shell=False)


def like_multi(chromosome, region):
    """Runs harp like function in parallel"""
    bam_file_list = [xfiles.bams_gen0['Gen0A'], xfiles.bams_gen0['Gen0B']]
    pool = Pool(21, limit_cpu)
    adjusted_func = partial(like_process, chromosome, region)
    pool.map(adjusted_func, bam_file_list)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
