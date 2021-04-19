"""Determines parameters to determine good window size for estimating
haplotype frequency"""
import presimulation.recombination.convert_recmap as converter
import presimulation.forqsprep.config as config
import forqs.forqs_parallel as forqs
import presimulation.forqsprep.forq_organizer as forg
import presimulation.forqsprep.recombination_search as rcount


class PreSimParam:
    """Take in the initial simulation parameters and determine
    maximum window with minimal recombination"""

    def __init__(self, chromosome, window, simulation_number):
        self.contig = chromosome
        self.region = window
        self.simulation_number = simulation_number
        self.region_length = None
        self.active = True
        self.update_state = None
        self.recombination_number = None

    def length(self):
        """Gets length of region over which simulation is going to occur"""
        self.region_length = len(range(self.region[0], self.region[1] + 1))

    def update(self, recombination_count):
        """Update region if recombination_count is > 10"""
        if recombination_count > 0.00001:
            self.region_length = self.region_length - round(self.region_length * 0.05)
            new_region = (self.region[0], self.region[0] + self.region_length)
            self.region = new_region
            self.update_state = 0
        else:
            self.active = False
            self.update_state = 1

    def test_recombination(self):
        """Test for Recombination of a forqsprep run"""
        activate = 1
        while activate:
            self.length()
            recombination_map = converter.main_recmap(self.region, self.contig)
            config.main_preconfig(self.region_length, recombination_map, self.simulation_number)
            configs = config.list_simulation_configs()
            # print(configs)
            forqs.forqs_parallel(configs)
            finfo = forg.Organizer(self.contig, self.region, self.simulation_number)
            finfo.move_configs()
            self.recombination_number = rcount.counts(finfo.population_files)
            self.update(self.recombination_number)
            if not self.update_state:
                nfinfo = forg.Organizer(self.contig, self.region, self.simulation_number)
                forg.clean()
            else:
                self.length()
                # print(self.region_length)
                forg.clean()
                activate -= 1

    def try_recombination(self):
        """Try simulations along the length of the original sequence and """
        self.length()
        recombination_map = converter.main_recmap(self.region, self.contig)
        config.main_preconfig(self.region_length, recombination_map, self.simulation_number)
        configs = config.list_simulation_configs()
        # print(configs)
        forqs.forqs_parallel(configs)
        finfo = forg.Organizer(self.contig, self.region, self.simulation_number)
        finfo.move_configs()
        self.recombination_number = rcount.counts(finfo.population_files)
        forg.clean()


if __name__ == '__main__':
    pass
