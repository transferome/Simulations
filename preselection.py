import presimulation.regionblueprint as regionblueprint
import presimulation.harpinitial.harpfoundingfrequencies as estimatefounders
import presimulation.harpfinal.harpendingfrequencies as estimatesamples
import dirmaker.filemove as mover
import dirmaker.foldermove as fmover


def main(contig, region, recombination_simulation_number):
    bloop = regionblueprint.preselection_recombination(contig, region, recombination_simulation_number)
    estimatefounders.harp_estimate(bloop)
    estimatesamples.harp_final(bloop)
    mover.gen0freq()
    mover.expfst()
    mover.endfrqtxt()
    mover.simfilesmove(bloop)
    fmover.preselect_move(bloop)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Presimulation: Estimation Windows Program")
    parser.add_argument("-c", "--chr", help='chromosome')
    parser.add_argument("-b", '--begin', help='first position')
    parser.add_argument("-e", '--end', help='end position')
    parser.add_argument('-n', '--number', help='number of recombination simulations')
    args = parser.parse_args()
    cont = args.chr
    regi = (int(args.begin), int(args.end))
    main(cont, regi, int(args.number))
    # bloop = regionblueprint.preselection_recombination(cont, regi, 10)
