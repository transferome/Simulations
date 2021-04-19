"""  Dictionary to map samples to and chromosomes to different filenames 
for Harp to use"""
from . import resources


snps = {'2L': '{}/2L_snp_good.txt'.format(resources),
        '2R': '{}/2R_snp_good.txt'.format(resources),
        '3L': '{}/3L_snp_good.txt'.format(resources),
        '3R': '{}/3R_snp_good.txt'.format(resources)}


bams_gen0 = {'Gen0A': '{}/S21_sorted_proper_realigned.bam'.format(resources),
             'Gen0B': '{}/S22_sorted_proper_realigned.bam'.format(resources)}


bams = {'S1_sorted_proper_realigned.bam': 'Gen15Up1A', 'S2_sorted_proper_realigned.bam': 'Gen15Up2A',
        'S3_sorted_proper_realigned.bam': 'Gen15Dwn1A', 'S4_sorted_proper_realigned.bam': 'Gen15Dwn2A',
        'S5_sorted_proper_realigned.bam': 'Gen15CtrlA',
        'S6_sorted_proper_realigned.bam': 'Gen15Up1B', 'S7_sorted_proper_realigned.bam': 'Gen15Up2B',
        'S8_sorted_proper_realigned.bam': 'Gen15Dwn1B', 'S9_sorted_proper_realigned.bam': 'Gen15Dwn2B',
        'S10_sorted_proper_realigned.bam': 'Gen15CtrlB'}


reference = '{}/dmel-majchr-norm-r6.24.fasta'.format(resources)


def dictmkr():
    dictout = {'Gen15Up1A': None, 'Gen15Up2A': None,
               'Gen15Dwn1A': None, 'Gen15Dwn2A': None,
               'Gen15CtrlA': None,
               'Gen15Up1B': None, 'Gen15Up2B': None,
               'Gen15Dwn1B': None, 'Gen15Dwn2B': None,
               'Gen15CtrlB': None}
    return dictout


def endfiledict():
    # this dictionary guides the organization of the estimated frequencies at Gen15
    # outfile_dict = {'Gen15Up1A': None, 'Gen15Up2A': None,
    #                 'Gen15Dwn1A': None, 'Gen15Dwn2A': None,
    #                 'Gen15CtrlA': None,
    #                 'Gen15Up1B': None, 'Gen15Up2B': None,
    #                 'Gen15Dwn1B': None, 'Gen15Dwn2B': None,
    #                 'Gen15CtrlB': None}
    outfile_dict = dictmkr()
    outfiles = ['end{}_frequencies.txt'.format(key) for key in outfile_dict.keys()]
    for key in outfile_dict.keys():
        dictfile = [file for file in outfiles if key in file][0]
        outfile_dict[key] = dictfile
    return outfile_dict


if __name__ == '__main__':
    pass
