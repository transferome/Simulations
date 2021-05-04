"""Runs samtools sort in parallel on bam files"""
import simulations.simulatereads.cleansimreads as cleaner
import subprocess
from multiprocessing import Pool


def samtools_sort(bamfile):
    """Samtools sort command and process"""
    sorted_bam_file = '{}_sorted.bam'.format(bamfile.split('.bam')[0])
    command_list = ['samtools', 'sort', '-@4', bamfile, '-o', sorted_bam_file]
    command = ' '.join(command_list)
    # print(command)
    subprocess.call(command, shell=True)


def samtools_sort_multi(region_tag):
    """runs samtools view in parallel"""
    bams = cleaner.listbams(region_tag)
    pool = Pool(21)
    pool.map(samtools_sort, bams)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
