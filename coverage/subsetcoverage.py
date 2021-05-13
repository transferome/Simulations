import coverage.listcovfiles as cf


def subsetfiles():
    contigs = ['2R', '2L', '3R', '3L']
    cfiles = cf.listcov()
    for cfile in cfiles:
        for contig in contigs:
            f"{cfile.split('_')[0].split('/')[-1]}_{contig}"