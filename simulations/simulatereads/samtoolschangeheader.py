"""  Change Header of Samtools File from Melanogaster info to Simulans info
 needed for the simulatereads of D. simulans"""
import simulations.simulatereads.cleansimreads as cleaner
from multiprocessing import Pool


def changer(samfile):
    data = [line for line in open(samfile) if not line.startswith('@')]
    header_list = ['@SQ\tSN:2L\tLN:23513712\n',
                   '@SQ\tSN:2R\tLN:25286936\n',
                   '@SQ\tSN:3L\tLN:28110227\n',
                   '@SQ\tSN:3R\tLN:32079331\n',
                   '@SQ\tSN:X\tLN:235542271\n',
                   '@PG\tID:simreads\tPN:simreads\tVN:1.0\n']
    with open(samfile, 'w+') as newsam:
        for h in header_list:
            newsam.write(h)
        for s in data:
            newsam.write(s)


def samtools_change_multi(region_tag):
    """runs samtools view in parallel"""
    sams = cleaner.listsams(region_tag)
    pool = Pool(21)
    pool.map(changer, sams)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
