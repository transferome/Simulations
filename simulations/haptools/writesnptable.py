"""Writes out the constructed haplotypes in a SNP file acceptable to simulatereads"""


def write_snp_table(hapfile, final_haplotypes, constructor_tag):
    """Write the snp_table needed for simulatereads"""
    indi_nums = range(1, len(final_haplotypes[0].split(',')) + 1)
    indi_strs = [str(x) for x in indi_nums]
    indi_line = ','.join(indi_strs)
    header = ','.join([constructor_tag.contig, 'Ref', indi_line])
    with open(hapfile) as f, open(constructor_tag.output_snpfile, 'w+') as fo:
        fo.write('{}\n'.format(header))
        # fo.write('\n')
        for org, new in zip(f, final_haplotypes):
            org_info = ','.join(org.split('\t')[0:2])
            new_line = ','.join([org_info, new])
            fo.write('{}\n'.format(new_line))
            # fo.write('\n')


if __name__ == '__main__':
    pass
