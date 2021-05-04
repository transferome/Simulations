"""Clears crap files from the simulation run to get the founding frequency and
simulation frequencies for comparison"""
import os
import shutil


def clear_directories():
    """Clears the run directories created during the simulation process"""
    directories = [s for s in os.listdir() if os.path.isdir(s)]
    run_dirs = [s for s in directories if s.startswith('run')]
    for d in run_dirs:
        shutil.rmtree(d)


def clear_foundandsample(simreads_tags):
    """Removes the founding harp freq file for the region of the tags"""
    del_file = simreads_tags[0].founding_frequency_file.split('/')[-1]
    # os.remove(del_file)
    sample_file = '{}_rep{}.sample'.format(del_file.split('_')[0], simreads_tags[0].replicate)
    os.remove(sample_file)
    os.remove('forqs.seed')


def clear_simfreqs(simreads_tags):
    """clears the individual simulation frequency files"""
    for tag in simreads_tags:
        os.remove(tag.freq_file)


if __name__ == '__main__':
    pass
