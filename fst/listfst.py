"""  Lists Within, or Between Fst Files  """
import glob


def withinfiles(replicate='A'):
    """Returns the Fst within simulation Fst.  Which is Fst between
    simulated up and downs within a Replicate"""
    withins = glob.glob('*_Fst.txt')
    if replicate == 'A':
        files = [file for file in withins if 'RepA' in file]
        files.sort(key=lambda x: int(x.split('_')[0].split('-')[0]))
        return files
    else:
        files = [file for file in withins if 'RepB' in file]
        files.sort(key=lambda x: int(x.split('_')[0].split('-')[0]))
        return files


def betweenfiles():
    """Returns the Fst between replicate files"""
    betweens = glob.glob('*_Fst_between.txt')
    betweens.sort(key=lambda x: int(x.split('_')[0].split('-')[0]))
    return betweens


if __name__ == '__main__':
    pass
