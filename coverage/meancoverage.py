"""Opens a window coverage file and returns the mean and variance of the coverage in that window"""
import numpy as np


def get_coverage_mean(inputfile):
    with open(inputfile) as f:
        coverage_list = [int(line.split('\t')[2]) for line in f]
        mean_coverage = round(sum(coverage_list) / len(coverage_list), 8)
        variance_coverage = round(float(np.var(coverage_list))**0.5, 8)
    return mean_coverage, variance_coverage


# TODO: these would need changed for simulans because samples are different
def window_region_check(window_sample_dictionary):
    false_list = list()
    comparison_windows = window_sample_dictionary['S1']
    for key in window_sample_dictionary.keys():
        if not key == 'S1':
            check_windows = window_sample_dictionary[key]
            if check_windows == comparison_windows:
                false_list.append(True)
            else:
                false_list.append(False)
    return false_list


if __name__ == '__main__':
    pass
