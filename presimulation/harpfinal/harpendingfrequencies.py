"""  Runs harp and calculates frequencies in the window on all of the sample files
  at gen 15 as well.  In order to get average frequencies for comparison of Fst within that window  """
import presimulation.harpfinal.harpending as harpf
import presimulation.harpfinal.processfinal as sub
import presimulation.harpfinal.sumfreqend as summer
import fst.fstendfreqs as fst
import harpsnp.gen15combinedfreqs as combiner
import dirmaker.filemove as mover


def harp_final(blueprint):
    hpf = harpf.HarpEnd(blueprint)
    hpf.like()
    hpf.freq(blueprint.region_size)
    harpf.clean(blueprint)
    subsetter = sub.SplitEnds(blueprint)
    subsetter.split_end()
    endfreq = summer.SumFreqEnd(blueprint.chromosome)
    endfreq.sumf()
    subsetter.gather_end()
    fst.endfst()
    combined_files = combiner.endfreqs(blueprint)
    mover.combinemove(blueprint, combined_files)


if __name__ == '__main__':
    pass
