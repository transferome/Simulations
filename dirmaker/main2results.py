"""  Moves the main directory into the results directory  """
import dirmaker.directorymaker as dirmkdir
import subprocess


def move2results(blueprint):
    maindir = dirmkdir.main_dir(blueprint)
    subprocess.call(['mv', maindir, 'results/'], shell=False)


if __name__ == '__main__':
    pass
