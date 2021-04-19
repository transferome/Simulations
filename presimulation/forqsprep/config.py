"""Creates forqsprep config used to determine max sequence length without recombination, prior to running
simulations which simulate the artificial selection"""
from . import resource_file
import glob


def list_simulation_configs():
    """List all the directories created by forqsprep"""
    return glob.glob('run_*.config')


def read_template(template_resource):
    """ Read in the template file """
    template = [line for line in open(template_resource)]
    return template


def alter_template(forqs_template_list, contig_len, rec_rates, stem):
    """ Alter the Information required to run desired simulation """
    altered = list()
    for line in forqs_template_list:
        if 'chromosome_lengths' in line:
            new_line = line.replace('2799800', str(contig_len))
            altered.append(new_line)
        elif line.endswith('.csv\n'):
            new_line = line.replace('dmel_recRates_3L_5100200-7900000.csv', rec_rates)
            altered.append(new_line)
        elif 'output_directory' in line:
            new_line = line.replace('chr3L_0', 'run_{}'.format(str(stem)))
            altered.append(new_line)
        else:
            altered.append(line)
    return altered


def write_template(stem, altered_template_list):
    """Writes out the altered template and creates new config file"""

    with open('run_{}.config'.format(stem), 'w+') as f:
        for line in altered_template_list:
            f.write(line)


def main_preconfig(contig_len, rec_rates, simulation_number):
    for x in range(simulation_number):
        blueprint = read_template(resource_file)
        altered_config = alter_template(blueprint, contig_len, rec_rates, x)
        write_template(x, altered_config)


if __name__ == '__main__':
    pass
