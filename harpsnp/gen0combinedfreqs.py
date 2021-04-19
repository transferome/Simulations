"""  Organize the mean frequency of the haplotypes at generation 0 using the simreads tags
  needs to be used after the simread_sumfreq.py module"""

# class object will take the blueprint, replicate, and simreadstags
# blueprint and replicate only for naming the output file


class GenZeroCombined:

    def __init__(self, replicate):
        self.file = 'replicate{}_frequencies.txt'.format(replicate)
        self.outfile = 'Gen0{}_combined.freqs'.format(replicate)
        with open(self.file) as infile:
            textlines = [line for line in infile]
            textlines.sort(key=lambda x: int(x.split(',')[0].split('-')[0]))
        with open(self.outfile, 'w+') as output:
            for line in textlines:
                region = line.split(',')[0].split('-')[0]
                frequencies = line.split(',')[1:]
                frequencies.insert(0, region)
                output.write(','.join(frequencies))


if __name__ == '__main__':
    pass
