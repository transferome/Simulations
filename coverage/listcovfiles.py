"""Lists coverage files, they are in /home/ltjones/Simulations*/coverage/resources/"""
from . import resource_dir
import glob


def listcov():
    covfiles = glob.glob(f'{resource_dir}/*.coverage')
    covfiles.sort(key=lambda x: int(x.split('_')[0].split('/')[-1].lstrip('S')))
    return covfiles