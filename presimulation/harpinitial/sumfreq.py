"""Sum frequencies and add header to a subset freq file"""
import glob
import pandas as pd
import harpsnp.filedict as xfiles


class SumFreq:

    def __init__(self, chromosome):
        self.chromosome = chromosome
        freqs = glob.glob('*.freqs')
        self.freqs = [s for s in freqs if self.chromosome not in s]

    def get_header(self):
        """get the header from the snp text file given the chromosome"""
        with open(xfiles.snps[self.chromosome]) as infile:
            header = infile.readline().rstrip('\n')
            keep = header.split(',')[2:]
            new_header = [self.chromosome, 'start', 'end'] + keep
            return new_header

    def read_freq(self, freqfile):
        """read the freq file and give it a header"""
        headin = self.get_header()
        file = pd.read_csv(freqfile, sep=',', names=headin)
        return file

    def sumf(self):
        for freq in self.freqs:
            # print(freq)
            df = self.read_freq(freq)
            mean_vals = df.mean(axis=0).tolist()
            mean = ["{:.5f}".format(float(num)) for num in mean_vals]
            mean.insert(0, 'mean')
            var_vals = df.var(axis=0).tolist()
            var = ["{:.8f}".format(float(num)) for num in var_vals]
            var.insert(0, 'var')
            df.loc[len(df.index)] = mean
            df.loc[len(df.index)] = var
            df.to_csv(path_or_buf=freq, sep=',', header=True, index=False)


if __name__ == '__main__':
    pass
