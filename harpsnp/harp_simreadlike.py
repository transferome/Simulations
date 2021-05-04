"""Harp likelihood process on the sorted bam files
created by the simulatereads package"""
import subprocess
from multiprocessing import Pool
import harpsnp.filedict as xfiles


def like(simreads_tag):
    """Makes the command and calls it using a simulatereads tag"""
    harp_like_command = ['harp', 'like', '-I', '--bam', simreads_tag.final_bam,
                         '--region', simreads_tag.harp_region,
                         '--refseq', xfiles.reference, '--snps', xfiles.snps[simreads_tag.contig],
                         '--stem', simreads_tag.harp_tag]
    print(harp_like_command)
    subprocess.call(harp_like_command, shell=False)


def like_multi(simreads_tags):
    """Runs harp like function in parallel"""
    pool = Pool(21)
    pool.map(like, simreads_tags)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
