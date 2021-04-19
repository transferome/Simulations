"""Count the number of snps within a particular region of a chromosome"""
from . import resources


def count_snps(chromosome, region):
    """Count number of snps"""
    with open('{}/{}_snp_good.txt'.format(resources, chromosome)) as f:
        counter = 0
        for idx, line in enumerate(f):
            if idx > 0:
                if region[0] <= int(line.split(',')[0]) <= region[1]:
                    counter += 1
    return counter


if __name__ == '__main__':
    pass
