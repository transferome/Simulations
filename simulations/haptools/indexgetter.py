"""Finds index of snp positions within the"""


# TODO: Module currently not in use
def index_getter(start_position, end_position, position_index_list):
    """Given an upper and lower bound for a position, this finds the index value of the maximum index value
    which pasts the equality testing"""
    index_min = [tup[0] for tup in position_index_list if tup[1] >= start_position]
    index_max = [tup[0] for tup in position_index_list if tup[1] <= end_position]
    ind_min = min(index_min)
    ind_max = max(index_max)
    return ind_min, ind_max


if __name__ == '__main__':
    pass
