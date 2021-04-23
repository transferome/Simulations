"""Dictionary, each key is a number, 0 to 106, which maps to the 106 DGRP lines
in the snp_good.txt file.  Each key holds a list, which is the indexes"""
import random


def make_id_map(multivariate_sample_list):
    """creates list of the dgrp indexes (using 0 -106), using the
    multivariate sample"""
    id_map = list()
    for idx, amount in enumerate(multivariate_sample_list):
        numeric_amount = int(amount)
        templist = [str(idx) for _ in range(numeric_amount)]
        if len(templist) == 0:
            pass
        else:
            id_map.extend(templist)
    random.shuffle(id_map)
    key_list = list(enumerate(id_map, 0))
    founder_dict = {str(k): v for k, v in key_list}
    return founder_dict


if __name__ == '__main__':
    pass
