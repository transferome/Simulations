"""Finds fst between the repA and repB replicates for a region"""
import fst.listsimfreqs as lister
import fst.fstcalculate as fstcalc


def fst_between_file(repafile, repbfile):
    """Gets Fst between two files from repA and repB"""
    outdata = list()
    with open(repafile) as fileA, open(repbfile) as fileB:
        data = [line.rstrip('\n') for line in fileA if not line.startswith('gen0')]
        datb = [line.rstrip('\n') for line in fileB if not line.startswith('gen0')]
        for x, y in zip(data, datb):
            infoa = x.split(',')[0]
            infob = x.split(',')[0]
            if infoa == infob:
                freqsa = x.split(',')[1:]
                freqsb = y.split(',')[1:]
                fst_val = fstcalc.fst(freqsa, freqsb)
                outdata.append('{},{}\n'.format(infoa, str(fst_val)))
            else:
                print('Mismatch')
    return outdata


def write_fst_between(repafile, repbfile):
    """writes out the fst info after its been calculated"""
    regiona = repafile.split('_')[0]
    regionb = repbfile.split('_')[0]
    if regiona == regionb:
        fstdata = fst_between_file(repafile, repbfile)
        with open('{}_Fst_between.txt'.format(regiona), 'w+') as outputfile:
            for line in fstdata:
                outputfile.write(line)


def fst_between():
    zipped_files = lister.zip_freqs()
    for x, y in zipped_files:
        write_fst_between(x, y)


if __name__ == '__main__':
    fst_between()
