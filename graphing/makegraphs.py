"""  Make data from the frequency file so it can be graphed.
This will take the list of returned files from the EndFreqs objects in combinedfreqs.py"""
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import rcParams
from numpy import linspace
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


class HarpPlot:

    def __init__(self, filename, chromosome):
        """Gets the list of positions from the file"""
        self.filename = filename
        self.chromosome = chromosome
        # TODO: need to change this, graphing will need to be done on my machine, ohta doesn't have matplotlib
        with open(self.filename) as f:
            data = [line.rstrip('\n') for line in f]
        self.positions = [int(line.split(',')[0]) for line in data]
        self.start_position = self.positions[0]
        self.final_position = self.positions[-1] + (self.positions[1] - self.positions[0])
        if 'Gen15' in self.filename:
            self.title = 'Generation 15 {}'.format(filename.split('_')[0].split('15')[1])
        if 'Gen0' in self.filename:
            if 'A' in self.filename:
                self.title = 'Generation 0 ReplicateA'
            if 'B' in self.filename:
                self.title = 'Generation 0 ReplicateB'
        self.x_axis_label = 'Genomic Coordinate: Chromosome Arm {}'.format(self.chromosome)
        # not going to add 1, that way x coordinates won't double up
        self.row_range_list = [range(position, self.positions[i + 1]) for i, position in enumerate(self.positions[:-1])]
        # need to add the range for the final element in self.positions list (last line of file)
        # adding length of a region (they're all the same) to achieve that
        # no -1 because last subregions final coordinate does not start another region
        self.row_range_list.append(range(self.positions[-1], self.final_position))
        self.col_dict = {idx: None for idx, col in enumerate(data[0].split(','))}
        del self.col_dict[0]
        for key in self.col_dict.keys():
            freq_list = list()
            for line in data:
                freq_list.append(round(float(line.split(',')[key]), 4))
            self.col_dict[key] = freq_list
        self.fig = None
        self.ax = None
        self.ymax = None
        # adding colors consistent coloring
        self.dgrp_number_of_lines = len(list(self.col_dict.keys()))
        cm_subsection = linspace(0, 1, self.dgrp_number_of_lines)
        self.colormap = [cm.gist_rainbow(x) for x in cm_subsection]
        self.graph_file = '{}_frequencies.png'.format(self.filename.split('_')[0])

    def find_ymax(self):
        max_val = 0
        for key in self.col_dict.keys():
            freqs_check = self.col_dict[key]
            new_max = round(max(freqs_check), 2)
            if new_max > max_val:
                max_val = new_max
        self.ymax = round(max_val, 2)
        # print(str(self.ymax))

    def easy_ymax(self):
        self.ymax = 1.0

    def plot(self):
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 10))
        self.ax.set_ylim([0, self.ymax + 0.05])
        xlim = len(range(1, 1000)) * len(self.row_range_list)
        self.ax.set_xlim([1, xlim])
        self.ax.set_title(self.title, fontsize=20)
        for key, color_iterator in zip(self.col_dict.keys(), self.colormap):
            y_data = list()
            for rng, freq in zip(self.row_range_list, self.col_dict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            self.ax.plot(range(1, xlim + 1), y_data, color=color_iterator, linewidth=5.0)
        # self.ax.set_xticks([idx for idx, s in enumerate(self.positions)])
        xticks = list(range(1, xlim, 1000))
        xticklables = ["{:,}".format(x) for x in self.positions]
        # yrange = range(0, self.ymax + 0.05, 0)
        # yticks = [0.2, 0.4, 0.6, 0.8]
        # yticklabels = ['0.2', '0.4', '0.6', '0.8']
        self.ax.set_xticks(xticks[0::4])
        self.ax.set_xticklabels(xticklables[0::4])
        # self.ax.set_yticks(yticks)
        # self.ax.set_yticklabels(yticklabels)
        plt.setp(self.ax.get_xticklabels(), fontsize=14)
        plt.setp(self.ax.get_yticklabels(), fontsize=14)
        self.ax.set_ylabel('Founding Simulans Haplotype Frequencies', fontsize=16)
        self.ax.set_xlabel(self.x_axis_label, fontsize=16)


# TODO: Easy and Find ymax are here
def plot_freqs(combined_file_list, chromosome):
    for comb in combined_file_list:
        hplot = HarpPlot(comb, chromosome)
        hplot.easy_ymax()
        hplot.plot()
        hplot.fig.savefig(hplot.graph_file, bbox_inches='tight')
        plt.clf()


if __name__ == '__main__':
    import os
    import glob
    # graph_folders = glob.glob('/home/solid-snake/Data/sim_simulations2018/2R/testdat/*_data2graph')
    # for folder in graph_folders:
    #     os.chdir(folder)
    #     combined_files = glob.glob('*combined.freqs')
    #     plot_freqs(combined_files, '2R')
    os.chdir('Exp_Haplotype_Frequency_Estimates')
    combined_files = glob.glob('*combined.freqs')
    plot_freqs(combined_files, '2R')
