"""Writes config for a simulatereads simulation"""
import harpsnp.filedict as xfiles


def frequency_string():
    """Creates a string of frequencies given the number sampled for simulatereads,
    this will always be 200"""
    temp = [1/200 for _ in range(0, 200)]
    normed = [x/sum(temp) for x in temp]
    return ' '.join([str(x) for x in normed])


def simreads_config(simreads_tag):
    """Writes out simreads_config using the simreads_tag"""
    file_lines = ['#', '#Usage:harp sim_reads', '#', '',
                  'filename_refseq {}'.format(xfiles.reference),
                  'filename_snps {}'.format(simreads_tag.haplotype_file),
                  'filename_stem {}_simreads'.format(simreads_tag.tag),
                  'region {}:{}-{}'.format(simreads_tag.contig, str(simreads_tag.min_max[0]), str(simreads_tag.min_max[1])),
                  'haplotype_frequencies {}'.format(frequency_string()), 'recombined haplotype frequencies',
                  'coverage 200', 'error_rate 0.00005', 'read_length 150']
    with open(simreads_tag.config_file, 'w+') as f:
        for line in file_lines:
            f.write('{}\n'.format(line))


if __name__ == '__main__':
    pass
