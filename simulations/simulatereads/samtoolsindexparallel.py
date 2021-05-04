"""Index the sorted sam files in parallel"""
import simulations.simulatereads.cleansimreads as cleaner
from multiprocessing import Pool
import subprocess


def samtools_index(bam_file):
    """Samtools index command and process"""
    command_list = ['samtools', 'index', '{}.bam'.format(bam_file.split('.bam')[0])]
    command = ' '.join(command_list)
    subprocess.call(command, shell=True)


def samtools_index_multi(region_tag):
    """runs samtools index in parallel"""
    bams = cleaner.listbams(region_tag)
    pool = Pool(21)
    pool.map(samtools_index, bams)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
