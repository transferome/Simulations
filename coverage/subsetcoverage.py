from . import resource_dir
import glob


def subsetfiles():
    contigs = ['2R', '2L', '3R', '3L']
    cfiles = glob.glob(f"{resource_dir}/*.coverage")
    for contig in contigs:
        for cfile in cfiles:
            # cov_file = f"{resource_dir}/{cfile}"
            new_file = f"{cfile.split('_')[0]}_{contig}.txt"
            print(new_file, cfile)
            with open(cfile) as inputf, open(new_file, 'w+') as outputf:
                tempdata = [x for x in inputf if int(x.split('\t')[2]) > 8]
                for line in tempdata:
                    if line.startswith(contig):
                        outputf.write(line)


if __name__ == '__main__':
    subsetfiles()
