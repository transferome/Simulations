import fst.fstbetweenreplicate as fstbetweenf
import fst.avgfst as avg


def fst_betweenreplicate():
    fstbetweenf.fst_between()


def average_fst(contig, pos1, pos2):
    avgblp = avg.AvgFst(contig, pos1, pos2)
    avgblp.files_regions()
    avgblp.gather_data()
    avgblp.write_sum()


if __name__ == '__main__':
    pass
