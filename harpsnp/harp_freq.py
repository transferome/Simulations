"""Multiprocessing of harp freq command"""
import subprocess
from multiprocessing import Pool
from functools import partial
import glob


def make_step(width):
    """Creates a step that is 10% of the window size"""
    return str(round(width * 0.10))


def freq_process(region, width, hlk_file):
    """Executes harps freq command"""
    # harp_freq_command = ['harp', 'freq', '--hlk', hlk_file, '--region', region, '--window_step',
    #                      make_step(width), '--window_width', str(width)]
    subprocess.check_call(['harp', 'freq', '--hlk', hlk_file, '--region', region, '--window_step',
                           make_step(width), '--window_width', str(width)], stdout=subprocess.DEVNULL, shell=False)


def freq_multi(region, width, gen='Gen0'):
    """runs harp freq in parallel multiprocess"""
    if gen == 'Gen0':
        hlks = glob.glob('*_Gen0*.hlk')
    else:
        hlks = glob.glob('*Gen15*.hlk')
    pool = Pool(21)
    adjusted_func = partial(freq_process, region, width)
    pool.map(adjusted_func, hlks)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
