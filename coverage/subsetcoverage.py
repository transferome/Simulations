import glob


def subsetfiles():
    contigs = ['2R', '2L', '3R', '3L']
    cfiles = glob.glob('coverage/resources/*.coverage')
    for contig in contigs:
        for cfile in cfiles:
            new_file = 'coverage/resources/{}_{}.txt'.format(contig, cfile.split('_')[0].split('/')[-1])
            print(new_file, cfile)
            with open(cfile) as inputf, open(new_file, 'w+') as outputf:
                for line in inputf:
                    print(line)
                    if line.startswith(contig):
                        outputf.write(line)


if __name__ == '__main__':
    subsetfiles()
