"""  Module  """
import glob
import math
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.lines import Line2D

# on linux
rcParams['font.family'] = "DejaVu Sans Mono"
# on windows
# rcParams['font.family'] = "monospace"


plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "white",
    "axes.facecolor": "black",
    "axes.edgecolor": "white",
    "axes.labelcolor": "white",
    "xtick.color": "goldenrod",
    "ytick.color": "goldenrod",
    "grid.color": "black",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "font.monospace": "monospace",
    "savefig.edgecolor": "black",
    "figure.max_open_warning": 0})


class FstData:
    def __init__(self, fstfile, chromosome, simulated=False):
        self.data = None
        self.simulated = False
        if not simulated:
            with open(fstfile) as f:
                self.data = [line.rstrip('\n') for line in f]
        else:
            self.simulated = True
            with open(fstfile) as f:
                self.data = [line.rstrip('\n') for line in f if not line.startswith('region')]
        self.pos1 = [int(line.split(',')[0].split('-')[0]) for line in self.data]
        self.pos2 = [int(line.split(',')[0].split('-')[1]) for line in self.data]
        self.startpos = self.pos1[0]
        self.endpos = self.pos2[-1]
        self.region = '{}:{}-{}'.format(chromosome, str(self.startpos), str(self.endpos))
        self.dict = None

    def dictionary(self):
        self.dict = {idx: None for idx, col in enumerate(self.data[0].split(','))}
        del self.dict[0]
        for key in self.dict.keys():
            fst_list = list()
            for line in self.data:
                fst_list.append(round(float(line.split(',')[key]), 4))
            self.dict[key] = fst_list

    def max(self, maxval):
        tracker = maxval
        for key in self.dict.keys():
            freqs_check = self.dict[key]
            new_max = round(max(freqs_check), 2)
            if new_max > tracker:
                tracker = new_max
        return tracker


class FstClass:

    def __init__(self, chromosome):
        """Gets the list of positions from the file"""
        self.chromosome = chromosome
        self.expdat1A_ud = 'Exp_Up1A_Dwn1A_Fst.dat'
        self.expdat2A_ud = 'Exp_Up2A_Dwn2A_Fst.dat'
        # self.expdatUpB1 = 'Exp_Up1B_CtrlB_Fst.dat'
        # self.expdatUpB2 = 'Exp_Up2B_CtrlB_Fst.dat'
        self.expdat1B_ud = 'Exp_Up1B_Dwn1B_Fst.dat'
        self.expdat2B_ud = 'Exp_Up2B_Dwn2B_Fst.dat'
        # self.expdatDwnB1 = 'Exp_Dwn1B_CtrlB_Fst.dat'
        # self.expdatDwnB2 = 'Exp_Dwn2B_CtrlB_Fst.dat'
        self.cdat = 'Exp_CtrlA_CtrlB_Fst.dat'
        self.simdat = glob.glob('*_Simulation_Fst.dat')[0]
        self.region = None
        self.expdat1A_udobj = FstData(self.expdat1A_ud, self.chromosome)
        self.expdat2A_udobj = FstData(self.expdat2A_ud, self.chromosome)
        # self.expdatUpB1obj = FstData(self.expdatUpB1, self.chromosome)
        # self.expdatUpB2obj = FstData(self.expdatUpB2, self.chromosome)
        self.expdat1B_udobj = FstData(self.expdat1B_ud, self.chromosome)
        self.expdat2B_udobj = FstData(self.expdat2B_ud, self.chromosome)
        # self.expdatDwnB1obj = FstData(self.expdatDwnB1, self.chromosome)
        # self.expdatDwnB2obj = FstData(self.expdatDwnB2, self.chromosome)
        self.cdatobj = FstData(self.cdat, self.chromosome)
        self.simdatobj = FstData(self.simdat, self.chromosome, simulated=True)

        if self.expdat1A_udobj.region == self.expdat2A_udobj.region:
            if self.expdat1B_udobj.region == self.expdat2B_udobj.region:
                self.region = self.expdat1A_udobj.region
            else:
                print("Problem")
                quit()
        else:
            print('Problem')
            quit()
        self.expdat1A_udobj.dictionary()
        self.expdat2A_udobj.dictionary()
        # self.expdatUpB1obj.dictionary()
        # self.expdatUpB2obj.dictionary()
        self.expdat1B_udobj.dictionary()
        self.expdat2B_udobj.dictionary()
        # self.expdatDwnB1obj.dictionary()
        # self.expdatDwnB2obj.dictionary()
        self.cdatobj.dictionary()
        self.simdatobj.dictionary()

        self.range_list = list()
        for a, b in zip(self.expdat1A_udobj.pos1, self.expdat1A_udobj.pos2):
            # subtract 1, so that range
            self.range_list.append(range(a, b))
        self.outputfile = 'Fst_data.png'
        # self.title = 'Comparing Up & Down Haplotype Frequencies (1Kb windows)'
        self.x_label = 'Genomic Coordinate: Chromosome Arm {}'.format(self.chromosome)
        # TODO: need to add variance to Fst when calculating so you can make error bars in graph (possibly)
        self.y_label = 'Fst (Between Haplotype Frequency Windows)'
        self.fig = None
        self.ax = None
        self.ymax = None
        self.simcolormap = ['honeydew']
        self.expdatAcolormap = ['orangered']
        self.expdatBcolormap = ['mediumslateblue']
        # self.expdatDwnAcolormap = ['orange']
        # self.expdatDwnBcolormap = ['mediumorchid']
        self.ctrlcolormap = ['navajowhite']
        # self.expdatBcolormap = ['pink']
        # self.expdatDwnAcolormap = ['chartreuse']
        # self.expdatDwnBcolormap = ['yellowgreen']

    def find_ymax(self):
        max_val = self.expdat1A_udobj.max(0)
        max_val = self.expdat2A_udobj.max(max_val)
        # max_val = self.expdatUpB1obj.max(max_val)
        # max_val = self.expdatUpB2obj.max(max_val)
        max_val = self.expdat1B_udobj.max(max_val)
        max_val = self.expdat2B_udobj.max(max_val)
        # max_val = self.expdatDwnB1obj.max(max_val)
        # max_val = self.expdatDwnB2obj.max(max_val)
        max_val = self.cdatobj.max(max_val)
        max_val = self.simdatobj.max(max_val)
        self.ymax = round(max_val, 2)
        # print(str(self.ymax))

    def easy_ymax(self):
        self.ymax = 0.99

    def plotfst(self, axis, datadict, coloriter, xlimit, alpha_val, linetype='-'):
        for key, color_iterator in zip(datadict.keys(), coloriter):
            y_data = list()
            for rng, freq in zip(self.range_list, datadict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            axis.plot(range(1, xlimit + 1), y_data, color=color_iterator, linestyle=linetype, alpha=alpha_val,
                      linewidth=3.5)

    def simfst(self, axis, datadict, color_iterator, xlimit, alpha_val, linetype='-'):
        for key in range(1, 3):
            y_data = list()
            e_data = list()
            # err_key = key + 3
            err_list = datadict[key + 2]
            # TODO: sample size will change
            errlst = [1.96*(math.sqrt(x)/math.sqrt(40)) for x in err_list]
            for rng, freq, er in zip(self.range_list, datadict[key], errlst):
                y_data.extend([freq for _ in range(1, 1000)])
                e_data.extend([(freq + er, freq - er) for _ in range(1, 1000)])
            e_data0 = [tup[0] for tup in e_data]
            e_data1 = [tup[1] for tup in e_data]
            axis.plot(range(1, xlimit + 1), y_data, color=color_iterator[0], linestyle=linetype, alpha=alpha_val,
                      linewidth=3.5)
            axis.fill_between(range(1, xlimit + 1), e_data0, e_data1, color=color_iterator, alpha=alpha_val)

    def plot(self):
        self.fig, self.ax = plt.subplots(nrows=1, ncols=2, figsize=(30, 10))
        self.ax[0].set_ylim([0, self.ymax + 0.05])
        self.ax[1].set_ylim([0, self.ymax + 0.05])

        xlim = len(range(1, 1000)) * len(self.range_list)
        self.ax[0].set_xlim([1, xlim])
        self.ax[1].set_xlim([1, xlim])
        # self.ax.set_title(self.title, fontsize=20)
        self.plotfst(self.ax[0], self.expdat1A_udobj.dict, self.expdatAcolormap, xlim, 1.0)
        self.plotfst(self.ax[0], self.expdat2A_udobj.dict, self.expdatAcolormap, xlim, 0.5)
        # self.plotfst(self.ax[0], self.expdatUpB1obj.dict, self.expdatBcolormap, xlim, 1.0)
        # self.plotfst(self.ax[0], self.expdatUpB2obj.dict, self.expdatBcolormap, xlim, 0.5)
        self.plotfst(self.ax[1], self.expdat1B_udobj.dict, self.expdatBcolormap, xlim, 1.0)
        self.plotfst(self.ax[1], self.expdat2B_udobj.dict, self.expdatBcolormap, xlim, 0.5)
        # self.plotfst(self.ax[1], self.expdatDwnB1obj.dict, self.expdatDwnBcolormap, xlim, 1.0)
        # self.plotfst(self.ax[1], self.expdatDwnB2obj.dict, self.expdatDwnBcolormap, xlim, 0.5)
        self.simfst(self.ax[0], self.simdatobj.dict, self.simcolormap, xlim, 0.8, '--')
        self.simfst(self.ax[1], self.simdatobj.dict, self.simcolormap, xlim, 0.8, '--')
        self.plotfst(self.ax[0], self.cdatobj.dict, self.ctrlcolormap, xlim, 0.8, '--')
        self.plotfst(self.ax[1], self.cdatobj.dict, self.ctrlcolormap, xlim, 0.8, '--')

        custom_lines1 = [Line2D([0], [0], color='orangered', lw=4, label='Up1A v Dwn1A'),
                         Line2D([0], [0], color='orangered', lw=4, alpha=0.5, label='Up2A v Dwn2A'),
                         Line2D([0], [0], color='navajowhite', lw=4, alpha=0.8, linestyle='--', label='Control'),
                         Line2D([0], [0], color='honeydew', lw=4, alpha=0.8, label='Simulations')]
        custom_lines2 = [Line2D([0], [0], color='mediumslateblue', lw=4, label='Up1B v Dwn1B'),
                         Line2D([0], [0], color='mediumslateblue', lw=4, alpha=0.5, label='Up2B v Dwn2B'),
                         Line2D([0], [0], color='navajowhite', lw=4, linestyle='--', alpha=0.8, label='Control'),
                         Line2D([0], [0], color='honeydew', lw=4, alpha=0.8, label='Simulations')]
        # self.ax.set_xticks([idx for idx, s in enumerate(self.positions)])
        xticks = list(range(1, xlim, 1000))
        xticklables = ["{:,}".format(x) for x in self.expdat1A_udobj.pos1]
        # yrange = range(0, self.ymax + 0.05, 0)
        # yticks = [0.2, 0.4, 0.6, 0.8]
        # yticklabels = ['0.2', '0.4', '0.6', '0.8']
        legen1 = self.ax[0].legend(fontsize=13, handles=custom_lines1, loc='upper left')
        legen2 = self.ax[1].legend(fontsize=13, handles=custom_lines2, loc='upper left')

        plt.setp(legen1.get_texts(), color='w')
        plt.setp(legen2.get_texts(), color='w')

        self.ax[0].set_xticks(xticks[0::25])
        self.ax[0].set_xticklabels(xticklables[0::25])
        plt.setp(self.ax[0].get_xticklabels(), fontsize=10)
        plt.setp(self.ax[0].get_yticklabels(), fontsize=13)
        self.ax[0].set_ylabel(self.y_label, fontsize=15)
        self.ax[0].set_xlabel(self.x_label, fontsize=15)
        self.ax[1].set_xticks(xticks[0::25])
        self.ax[1].set_xticklabels(xticklables[0::25])
        plt.setp(self.ax[1].get_xticklabels(), fontsize=10)
        plt.setp(self.ax[1].get_yticklabels(), fontsize=13)
        # self.ax[1].set_ylabel(self.y_label, fontsize=17)
        self.ax[1].set_xlabel(self.x_label, fontsize=15)


if __name__ == '__main__':
    import os
    contig = '2L'
    # listA = list(range(5, 32, 2))[:-1]
    # listB = list(range(5, 32, 2))[1:]
    x1 = 500000
    x2 = 23093611
    # x2 = 3
    # for x1, x2 in zip(listA, listB):
    os.chdir(f'C:\\Users\\ltjon\\Data\\Mel2018_Experimental_Haplotype_Graphs\\{contig}_{x1}-{x2}\\Fst_data')
    # os.chdir(f'/home/solid-snake/Data/mel_simulations2018/{contig}/testdat/{contig}_{x1}000000-{x2}000000_Fst')
    plotobj = FstClass(contig)
    plotobj.easy_ymax()
    plotobj.plot()
    os.chdir(f'C:\\Users\\ltjon\\Data\\Mel2018_Experimental_Haplotype_Graphs\\{contig}_{x1}-{x2}')
    plotobj.fig.savefig(f'{contig}_{x1}-{x2}_UpvDown_Fst.png', bbox_inches='tight')
    plt.clf()
