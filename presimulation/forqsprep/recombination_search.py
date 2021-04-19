"""Search for Recombination within Population Files From forqsprep"""


def counts(population_file_list):
    """Read in a pop file and return the number of recombination events"""
    number_of_populations = len(population_file_list)
    number_of_individuals = 2000
    total_individual = number_of_populations * number_of_individuals
    recombinants = 0
    for file in population_file_list:
        with open(file) as f:
            for line in f:
                if ') (' in line:
                    recombinants += 1
    percentage_recombinants = round(recombinants/total_individual, 5)
    return percentage_recombinants


if __name__ == '__main__':
    pass
