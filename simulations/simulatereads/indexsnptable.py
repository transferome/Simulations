"""Multiprocessing of Index Snp Table program from harp-simulatereads"""
import subprocess
from multiprocessing import Pool


def index_snp_texts(snp_text):
    """index snp table process"""
    # print(command)
    subprocess.call(['/usr/local/bin/index_snp_table', snp_text, '1000'], shell=False)


def index_snp_multi(simreadstags):
    """Index multiple SNP files at same time """
    snp_texts = [simreadstag.haplotype_file for simreadstag in simreadstags]
    pool = Pool(21)
    pool.map(index_snp_texts, snp_texts)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
