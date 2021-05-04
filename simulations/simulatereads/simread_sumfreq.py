"""Sums frequency files created by simulatereads freq to get estimate
 of haplotype in region"""
import pandas as pd
import harpsnp.filedict as xfiles


def subsetfreq(simreads_tag):
    """Write out subset file"""
    subset_list = list()
    with open(simreads_tag.freq_file) as freq:
        for line in freq:
            split_line = line.split(' ')
            test_range = range(int(split_line[1]), int(split_line[2]))
            window_range = range(simreads_tag.region[0], simreads_tag.region[1])
            overlap_amount = len(range(max(window_range[0], test_range[0]), min(window_range[-1], test_range[-1]) + 1))
            overlap_percentage = round(overlap_amount/simreads_tag.region_length, 2)
            # if window[2] in test_range and window[3] in test_range:
            if overlap_percentage > 0.74:
                temp_line = line.split(' ')[:-1]
                subset_list.append('{}\n'.format(','.join(temp_line)))
    with open(simreads_tag.freq_file, 'w+') as newfreq:
        for line in subset_list:
            newfreq.write(line)


def get_header(simreads_tag):
    """get the header from the snp text file given the chromosome"""
    with open(xfiles.snps[simreads_tag.contig]) as infile:
        header = infile.readline().rstrip('\n')
        keep = header.split(',')[2:]
        new_header = [simreads_tag.contig, 'start', 'end'] + keep
        return new_header


def read_freq(simreads_tag):
    """read the freq file and give it a header"""
    headin = get_header(simreads_tag)
    file = pd.read_csv(simreads_tag.freq_file, sep=',', names=headin)
    return file


def sumfreq(simreads_tag):
    """Sums frequencies in the freq files"""
    subsetfreq(simreads_tag)
    df = read_freq(simreads_tag)
    mean_vals = df.mean(axis=0).tolist()
    mean = ["{:.5f}".format(float(num)) for num in mean_vals]
    mean.insert(0, 'mean')
    var_vals = df.var(axis=0).tolist()
    var = ["{:.8f}".format(float(num)) for num in var_vals]
    var.insert(0, 'var')
    df.loc[len(df.index)] = mean
    df.loc[len(df.index)] = var
    df.to_csv(path_or_buf=simreads_tag.freq_file, sep=',', header=True, index=False)


def sumtag_freqs(simreads_tags):
    """Processes all the freq files for simulatereads tags"""
    for tag in simreads_tags:
        sumfreq(tag)


if __name__ == '__main__':
    pass

