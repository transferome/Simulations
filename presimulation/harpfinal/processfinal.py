"""  Handles the end of the estimation of frequencies at generation 15  """
import harpsnp.filedict as xfiles
import presimulation.harpinitial.processinitial as base
import dirmaker.directorymaker as cdir
import glob


class SplitEnds(base.SplitFreqs):
    """Sorts results of the Generation 15 harp frequencies"""

    def __init__(self, blueprint):
        super(SplitEnds, self).__init__(blueprint)
        self.blueprint_file = blueprint.file
        self.window_list = list()
        self.freq = glob.glob('{}/*Gen15*.freqs'.format(cdir.expfreq_dir()))
        self.sampledict = xfiles.dictmkr()
        for key in self.sampledict.keys():
            freqfile = [file for file in self.freq if key in file]
            self.sampledict[key] = freqfile[0]
        self.endict = xfiles.endfiledict()

    def subset_end(self, window):
        """Subsets the frequency file given a window, and replicate info"""
        for key in self.sampledict.keys():
            infile = self.sampledict[key]
            outfile = '{}-{}_Gen15_{}.freqs'.format(str(window[0]), str(window[1]), key)
            self.write(infile, outfile, window)

    def split_end(self):
        """ Splits the windows and sample types"""
        self.get_windows()
        for win in self.window_list:
            self.subset_end(win)

    def gather_end(self):
        """list either all of the A replicate freq files or the B replicate freq files"""
        for key in self.sampledict.keys():
            fout = self.endict[key]
            freqs = glob.glob('*{}*.freqs'.format(key))
            # this will remove files that were used to create the subset region freq files
            freqs = [file for file in freqs if ":" not in file]
            outputlist = list()
            for freq in freqs:
                with open(freq) as f2:
                    frequencies = [line.rstrip('\n') for line in f2 if line.startswith('mean')][0]
                    frequencies = frequencies.split(',')[3:]
                    regawn = freq.split('_')[0]
                    outputlist.append('{}\n'.format(','.join([regawn] + frequencies)))
            outputlist.sort(key=lambda x: int(x.split(',')[0].split('-')[0]))
            with open(fout, 'w+') as f1:
                for line in outputlist:
                    f1.write(line)


if __name__ == '__main__':
    pass
