"""  Finds the average fst value for each simulated region  """
import fst.listfst as lister
import numpy as np


def fstopen(fstfile):
    with open(fstfile) as f:
        fstlist = [float(line.rstrip('\n').split(',')[1]) for line in f]
    return fstlist


# function finds the average Fst within a between or within .txt file
def avgfst_between(fstfile):
    """Return the mean fst from an fst file"""
    fstlist = fstopen(fstfile)
    return str(round(sum(fstlist)/len(fstlist), 8))


def varfst_between(fstfile):
    """Return the variance in fst from an fst file"""
    fstlist = fstopen(fstfile)
    return str(round(float(np.var(fstlist, ddof=1)), 8))


def avgfst_within(fst1, fst2):
    fstlist1 = fstopen(fst1)
    fstlist2 = fstopen(fst2)
    fstlist = fstlist1 + fstlist2
    return str(round(sum(fstlist)/len(fstlist), 8))


def varfst_within(fst1, fst2):
    fstlist1 = fstopen(fst1)
    fstlist2 = fstopen(fst2)
    fstlist = fstlist1 + fstlist2
    return str(round(float(np.var(fstlist, ddof=1)), 8))


# this will take the blueprint object, which holds the information on the
# original window and contig
class AvgFst:
    """Calculates Average Fst for each region file and adds it to a list
    Methods for working with that list object into a data file"""

    def __init__(self, contig, pos1, pos2):
        """Sets up an id tag simulation_window given the blueprint,
        also a keyword argument that will be within or between"""
        self.contig = contig
        self.window = (pos1, pos2)
        self.simulation_window = '{}_{}-{}'.format(self.contig, str(self.window[0]), str(self.window[1]))
        self.repAwithins = None
        self.repBwithins = None
        self.betweens = None
        self.regions = None
        self.fst_data = ['region,withinFst_mean,betweenFst_mean,withinFst_var,betweenFst_var\n']

    def files_regions(self):
        """ Gets the files"""
        self.repAwithins = lister.withinfiles(replicate='A')
        self.repBwithins = lister.withinfiles(replicate='B')
        self.betweens = lister.betweenfiles()
        self.regions = [s.split('_')[0] for s in self.betweens]

    def gather_data(self):
        for w, x, y, z in zip(self.regions, self.repAwithins, self.repBwithins, self.betweens):
            self.fst_data.append('{}\n'.format(','.join([w, avgfst_within(x, y), avgfst_between(z), varfst_within(x, y),
                                                         varfst_between(z)])))

    def write_sum(self):
        """Writes out fstdata, 1 is repa within, 1 is repb within, final is
        between"""
        with open('{}_Simulation_Fst.dat'.format(self.simulation_window), 'w+') as output:
            for line in self.fst_data:
                output.write(line)


if __name__ == '__main__':
    pass
