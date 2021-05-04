"""Runs simulatereads on configs in parallel"""
import subprocess
from multiprocessing import Pool
from simulations.tags.constructortags import list_simreadsconifgs


def simreads(configfile):
    """The simulatereads command function"""
    sim_com = '/usr/local/bin/simreads'
    command = [sim_com, configfile]
    subprocess.call(command, shell=False)


def simreads_multi(constructor_tags):
    """Multiprocess of the simulatereads commands"""
    configs = list_simreadsconifgs(constructor_tags)
    pool = Pool(21)
    pool.map(simreads, configs)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
