import glob
import dirmaker.directorymaker as cdir
import harpsnp.harpclean as mover


class EndFreqs:

    def __init__(self):
        mover.move_freq()
        all_freqs = glob.glob('{}/*_Gen15_*.freqs'.format(cdir.expfreq_dir()))
        self.freq_dict = {'Gen15Up1A': None, 'Gen15Up2A': None,
                          'Gen15Dwn1A': None, 'Gen15Dwn2A': None,
                          'Gen15CtrlA': None,
                          'Gen15Up1B': None, 'Gen15Up2B': None,
                          'Gen15Dwn1B': None, 'Gen15Dwn2B': None,
                          'Gen15CtrlB': None}
        for key in self.freq_dict.keys():
            files = [s for s in all_freqs if '_Gen15_{}'.format(key) in s]
            files.sort(key=lambda x: int(x.split('/')[1].split('_')[0].split('-')[0]))
            self.freq_dict[key] = files
        self.output_files = list()

    def combine(self):
        for key, files in self.freq_dict.items():
            self.output_files.append('{}_combined.freqs'.format(key))
            with open('{}_combined.freqs'.format(key), 'w+') as output:
                for file in files:
                    position = file.split('/')[1].split('_')[0].split('-')[0]
                    mean_line = [line for line in open(file) if line.startswith('mean')][0]
                    output.write('{},{}'.format(position, ','.join(mean_line.split(',')[3:])))

    def return_files(self):
        """Outputs the list of combined files"""
        return self.output_files + ['Gen0A_combined.freqs', 'Gen0B_combined.freqs']


def endfreqs():
    """Function that a simulation run will use to handle the EndFreqs class"""
    endfreqobj = EndFreqs()
    endfreqobj.combine()
    return endfreqobj.return_files()


if __name__ == '__main__':
    pass
