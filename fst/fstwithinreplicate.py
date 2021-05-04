"""Calculates Fst between the up, down simulated frequencies held in the simulatereads tags
as the final_frequency_file.  First line in file is gen0 so it is ignored"""
import fst.fstcalculate as fstcalc


def pair_simulated_frequencies(simreads_tag):
    """Opens the simulatereads final freq file and pairs the up and down into a list"""
    with open(simreads_tag.final_frequency_file) as file:
        data = [line.rstrip('\n') for line in file][1:]
        # use even and odd to make pairs
        output_list = list()
        for idx, line in enumerate(data, 1):
            if not idx % 2 == 0:
                pair = (line, data[idx])
                output_list.append(pair)
            else:
                pass
    return output_list


def fst_dict(simreads_tag):
    """Returns fst value, and simulation sub information"""
    fstdict = {}
    data = pair_simulated_frequencies(simreads_tag)
    for pair in data:
        idx = None
        id1 = pair[0].split(',')[0].rstrip('u')
        id2 = pair[1].split(',')[0].rstrip('d')
        if id1 == id2:
            idx = id1
        else:
            print('Fst ID Mismatch')
            quit()
        freq1 = [float(s) for s in pair[0].split(',')[1:]]
        freq2 = [float(s) for s in pair[1].split(',')[1:]]
        fst_value = fstcalc.fst(freq1, freq2)
        fstdict[idx] = str(fst_value)
    return fstdict


def write_fst_dict(simreads_tag):
    """Write out the fst info using the simread_tag"""
    fstdic = fst_dict(simreads_tag)
    with open(simreads_tag.fst_compare, 'w+') as fstfile:
        for key in fstdic.keys():
            dataline = '{}\n'.format(','.join([key, fstdic[key]]))
            fstfile.write(dataline)


if __name__ == '__main__':
    pass
