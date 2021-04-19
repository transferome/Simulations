"""  Class Object to Run Harp Likelihood process on the gen 15 data  """
import subprocess
from multiprocessing import Pool
from functools import partial
from . import resources
from harpsnp.filedict import bams as sample_dict
from harpsnp.filedict import reference as ref_file
import harpsnp.filedict as xfiles
import psutil
import os


def limit_cpu():
    """Called at Every Process in Pool and sets niceness"""
    p = psutil.Process(os.getpid())
    p.nice(3)


def like_process(chromosome, region, gen15_bam):
    """Execute harp like command and process on particular
    Generation 15 bam file"""
    # use rangesubset to get min max SNP positions
    harp_like_command = ['harp', 'like', '--bam', '{}/{}'.format(resources, gen15_bam), '--region', region,
                         '--refseq', ref_file, '--snps', xfiles.snps[chromosome], '--stem',
                         '{}_{}'.format(region, sample_dict[gen15_bam])]
    # print(harp_like_command)
    subprocess.call(harp_like_command, shell=False)


def like_multi(chromosome, region):
    bam_files = list(sample_dict.keys())
    pool = Pool(21, limit_cpu)
    likef = partial(like_process, chromosome, region)
    pool.map(likef, bam_files)


if __name__ == '__main__':
    pass
