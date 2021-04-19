"""Organizer Class Module For Forqs Simulations"""
# import os
import glob
import shutil
import clear


def clean():
    """Remove the directories created by forqsprep and their contents"""
    clear.clean()


class Organizer:
    """Organizer Class Function To Move Through The Simulation Structure"""

    def __init__(self, contig, simulation_range, simulation_number):
        """Initialize Organizer Instance"""
        self.contig = contig
        self.range = simulation_range
        self.simulation_number = simulation_number
        self.simulation_directories = None
        items = glob.glob('run_*')
        dirs = [s for s in items if '.config' not in s]
        if len(dirs) == self.simulation_number:
            self.simulation_directories = sorted(dirs, key=lambda x: int(x.split('_')[1]))
        else:
            print('Error!: Simulation Number and Directory Number Are Not Equal')
        self.population_files = ['{}/population_final_pop1.txt'.format(directory) for directory
                                 in self.simulation_directories]

    def move_configs(self):
        """Move all of the config files created for forqsprep, into the forqsprep directory the config file created"""
        configs = glob.glob('run_*.config')
        configs_sorted = sorted(configs, key=lambda x: int(x.split('.')[0].split('_')[1]))
        if len(configs_sorted) == len(self.simulation_directories):
            for config_file, config_dir in zip(configs_sorted, self.simulation_directories):
                if config_file.split('.')[0].split('_')[1] == config_dir.split('_')[1]:
                    shutil.move(config_file, config_dir)
                else:
                    print('Forqs ID Numbers Dont Match')
        else:
            print('Different Number of Config Files and forqsprep Directories')


if __name__ == '__main__':
    pass
