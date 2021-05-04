"""Estimate haplotype frequencies in 100kb windows with
a 10kb step"""
import subprocess
from multiprocessing import Pool


def make_step(width):
    """Creates a step that is 10% of the window size"""
    return str(round(width * 0.10))


def freq_process(simreads_tag):
    """Executes harp freq command"""
    harp_freq_command = ['harp', 'freq', '--hlk', simreads_tag.hlk_file,
                         '--region', simreads_tag.harp_region, '--window_step',
                         make_step(simreads_tag.region_length), '--window_width', str(simreads_tag.region_length)]
    subprocess.check_call(harp_freq_command, shell=False)


def freq_multi(simreads_tags):
    """runs harp freq in parallel using the simreads_tags"""
    pool = Pool(21)
    pool.map(freq_process, simreads_tags)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
