import os


def subsetfiles():
    contigs = ['2R', '2L', '3R', '3L']
    cfiles_temp = os.listdir(r"coverage//resources")
    cfiles = [s for s in cfiles_temp if '__init__' not in s]
    for contig in contigs:
        for cfile in cfiles:
            cov_file = r"coverage//resources//{}".format(cfile)
            new_file = r'coverage//resources//{}_{}.txt'.format(contig, cfile.split('_')[0])
            print(new_file, cov_file)
            with open(cov_file) as inputf, open(new_file, 'w+') as outputf:
                tempdata = [x for x in inputf if int(x.split('\t')[2]) > 20]
                for line in tempdata:
                    if line.startswith(contig):
                        outputf.write(line)


if __name__ == '__main__':
    subsetfiles()
