"""Estimates frequencies and organizes them for the simulated bam files created from
simulations of the artificial selection at Gen0 to Gen 15"""
import harpsnp.harp_simreadfreq as harpfreq
import harpsnp.harp_simreadlike as harplike
import simulations.simulatereads.simread_sumfreq as simfreq
import fst.fstwithinreplicate as fstwithin


def simreads_harp(simreads_tags):
    """Runs simreads on the simulated frequencies, creates mean frequencies in fashion
    similar to founding frequencies, multiple windows that need to have 75% overlap with the
    region the mean frequency is for"""
    harplike.like_multi(simreads_tags)
    harpfreq.freq_multi(simreads_tags)
    simfreq.sumtag_freqs(simreads_tags)


def fst_whithinreplicate(simreads_tags):
    for tag in simreads_tags:
        fstwithin.write_fst_dict(tag)


if __name__ == '__main__':
    pass
