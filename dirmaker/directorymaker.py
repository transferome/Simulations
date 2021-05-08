""" Given the blueprint this will make a directory """
import os


def creator(pathname):
    if not os.path.exists(pathname):
        os.mkdir(pathname)
        return pathname
    else:
        return pathname


def main_dir(blueprint):
    path = '{}_{}-{}'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    return creator(path)


def misc_dir():
    path = 'misc_files'
    return creator(path)


def expfreq_dir():
    path = 'SourceData_Exp_Haplotype_Frequencies'
    return creator(path)


def fst_dir():
    path = 'Fst_data'
    return creator(path)


def exp_haplotype_estimate_dir():
    path = 'Exp_Haplotype_Frequency_Estimates'
    return creator(path)


def simulation_output_dir():
    path = 'Sim_Frequencies_Fst'
    return creator(path)


def results_experimental_dir(cont, pos1, pos2):
    return 'results/{}_{}-{}/Exp_Haplotype_Frequency_Estimates'.format(cont, str(pos1), str(pos2))


if __name__ == '__main__':
    pass
