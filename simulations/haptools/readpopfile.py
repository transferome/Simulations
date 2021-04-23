"""Read in a population.txt file created by forqs, in a way which it can be converted
into a fasta like haplotype sequence"""
from ast import literal_eval as make_tuple


def readpop(popfilename):
    """Reads in the popfile into usable data"""
    pop_file = [line.rstrip('\n') for line in open(popfilename)][2:]
    filtered_pop = list(filter(None, pop_file))
    new_list = list()
    for s in filtered_pop:
        if s.startswith('+ '):
            new_string = s.lstrip('+ { ')
            final_string = new_string.rstrip(' }')
            indi = final_string.split(' ')
            chunks = [make_tuple(s) for s in indi]
            new_list.append(chunks)
        if s.startswith('- '):
            new_string = s.lstrip('- { ')
            final_string = new_string.rstrip(' }')
            indi = final_string.split(' ')
            chunks = [make_tuple(s) for s in indi]
            new_list.append(chunks)
    return new_list


if __name__ == '__main__':
    pass
