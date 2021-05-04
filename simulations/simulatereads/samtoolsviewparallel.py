"""Samtools view in parallel"""
import simulations.simulatereads.cleansimreads as cleaner
import subprocess
from multiprocessing import Pool


def samtools_view(sam_file):
    """Samtools view command and process"""
    bam_file = '{}.bam'.format(sam_file.split('.sam')[0])
    command_list = ['samtools', 'view', '-bhS', sam_file, '>', bam_file]
    command = ' '.join(command_list)
    subprocess.call(command, shell=True)
    
    
def samtools_view_multi(region_tag):
    """runs samtools view in parallel"""
    sams = cleaner.listsams(region_tag)
    pool = Pool(21)
    pool.map(samtools_view, sams)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
