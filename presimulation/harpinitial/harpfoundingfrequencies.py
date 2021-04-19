"""Using the blueprint object, describing the regions in which to estimate
the starting haplotype frequencies, this function runs the harp programs
to estimate those frequencies, both from the A replicate gen0 data, and from
the B replicate gen0 data.
With both of these, haplotype frequencies are estimated over the subregions in one
harp run along the entire original window length.  The original window is extended
to 0.25 +/- the length of the region size in which recombination should not occur.
The harp frequency estimate is then done along the entire original window length,
in window widths that are the length determined by the prior simulations to be unaffected
by recombination.  A step of 10% of the window width is introduced.  This creates a scenario
where say given a region 8000000 - 10000000
That has a length of 2 million
Prior simulations show that recombination will leave window sizes up to 97kb untouched.
The region can thus be broken up into 97kb chunks like...
8000000 - 8097000, 8097000 - 8194000 ....
The assumption is haplotype frequencies are thus unrecombined within those windows.
However that is assuming the start point of 8000000 is the end of a chromosome.
It is not and so giving the 10% step, allows me to get the mean haplotype frequency in
the region of 8000000 - 8097000 through multiple harp frequency estimates which overlap
with that window but do not all completely overlap themselves.  In order for a frequency
window estimate, to be included in the mean estimate for a subregion window, it needs to overlap
with the subregion window by 75%.  Each subregion gets a mean estimate for the DGRP haplotypes
in that region in the Gen0 data for each replicate"""
import presimulation.harpinitial.harpfounding as harpi
import presimulation.harpinitial.processinitial as sub
import presimulation.harpinitial.sumfreq as summer
import harpsnp.gen0combinedfreqs as combiner

# import core.timetracer as timer


# @timer.timer(label='Harp')
def harp_estimate(blprint):
    hpl = harpi.Harp(blprint)
    hpl.freq(blprint.region_size)
    hpl.clean()
    subsetter = sub.SplitFreqs(blprint.file)
    subsetter.split(replicate='A')
    subsetter.split(replicate='B')
    suminit = summer.SumFreq(blprint.chromosome)
    suminit.sumf()
    subsetter.gatherfreq(replicate='A')
    subsetter.gatherfreq(replicate='B')
    combiner.GenZeroCombined(replicate='A')
    combiner.GenZeroCombined(replicate='B')


if __name__ == '__main__':
    pass
