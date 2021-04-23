"""Subsets fasta file into one for each of the major contigs"""
import harpsnp.filedict as xfiles

fasta_file = [line for line in open(xfiles.reference)]

contigs = ['>2L', '>2R', '>3L', '>3R', '>X']

idx_list = list()

for contig in contigs:
    for idx, line in enumerate(fasta_file):
        if line.startswith(contig):
            idx_list.append(idx)

for idy, contig in zip(idx_list, contigs):
    with open('harpsnp/resources/dmel-{}-norm-r6.24.fasta'.format(contig.lstrip('>')), 'w+') as output:
        output.write(fasta_file[idy])
        for line in fasta_file[idy + 1:]:
            if not line.startswith('>'):
                output.write(line)
            else:
                break

