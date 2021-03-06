"""Lists coverage files, they are in /home/ltjones/Simulations*/coverage/resources/"""
# from . import resource_dir
import glob


def listcov():
    covfiles = glob.glob(f'coverage/resources/*.coverage')
    covfiles.sort(key=lambda x: int(x.split('_')[0].split('/')[-1].lstrip('S')))
    return covfiles


def list_contig_files(contig):
    covfiles = glob.glob(f'coverage/resources/*{contig}.txt')
    return covfiles


def listsubsetcov(sample, contig, pos1, pos2):
    covfiles = glob.glob(f'results/{contig}_{pos1}-{pos2}/coverage/{sample}_{contig}_*.coverage')
    covfiles.sort(key=lambda x: int(x.split('/')[-1].split('_')[-1].split('-')[0]))
    return covfiles


if __name__ == '__main__':
    pass
