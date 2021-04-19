"""Run multiple preforqs simulations in parallel"""
import random
import subprocess
from multiprocessing import Pool


def forqs_sim(forqs_config):
    """Executes preforqs config file"""
    forqs_executable = '/usr/local/bin/forqs'
    # make a random seed, not really needed because preforqs writes a new random seed at end of each simulation
    forq_seed = 'seed={}'.format(str(random.randint(0, 32767)))
    subprocess.call([forqs_executable, forqs_config, forq_seed], stdout=subprocess.DEVNULL, shell=False)


def forqs_parallel(configs):
    """Execute preforqs in parallel"""
    pool = Pool(21)
    pool.map(forqs_sim, configs)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass

