"""One of main aspects of simulations for 2018.  This combines the presimparam and
blueprint class from preselct. Given a contig, region window as a tuple, and
number of simulations to run (number of iterations to test for recombination)
to determine the window size in which haplotypes will not have recombined within the region
, and gives a blueprint which has parameters describing the region to be simulated such as
The original window
The window size to estimate harp frequencies, and the different windows of that
size along the original window
Basically defines the subregions within the larger region that will be used to
estimate frequencies of DGRP haplotypes in the Gen0 data, and then run neutral
simulations given the selection experiment to simulate reads and harp frequencies
at simulated Generation 15 data"""
import presimulation.presimparam as sparam
import presimulation.blueprint as blprint


def preselection_recombination(chromosome, window, simulation_number):
    """Chromosome is a string
    Window is a tuple of integers
    simulation number is an integer"""
    blueprint = blprint.ParamBlueprint(chromosome, window, simulation_number,
                                       sparam.PreSimParam)
    blueprint.make()
    blueprint.write(window)
    return blueprint


if __name__ == '__main__':
    pass
