"""Takes a tag object and runs the forqs simulation on created config files"""
import forqs.forqs_parallel as fp
import shutil


class TagForqs:
    """Runs forqs in parallel on the created configs of a tag
    takes the list of configs in the attribute of TagConfigs"""

    def __init__(self, forqs_config_tag):
        self.tag = forqs_config_tag
        self.contig = forqs_config_tag.contig
        self.config_tag_list = forqs_config_tag.config_list
        self.subtags = forqs_config_tag.subtags
        self.region = forqs_config_tag.region
        self.region_length = forqs_config_tag.region_length
        self.recombination_file = forqs_config_tag.recombination_file
        self.simulation_number = forqs_config_tag.simulation_number
        fp.forqs_parallel(forqs_config_tag.config_list)

    def move_configs(self):
        """move config files into their created directories"""
        for tag in self.config_tag_list:
            shutil.move(tag, tag.split('.')[0])


if __name__ == '__main__':
    pass
