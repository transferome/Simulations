"""  Running Subregions in parallel  """
import simulations.processtags as tagger
import simulations.simulatereads.simreads as simreads
import simulations.harpsimulatedfrequencies as simharp
import harpsnp.harpclean as simclean


def subregion_processes(region_tags, pos1, pos2, replicate='A'):
    """processes the individual subregions created by the blueprint"""
    for region_tag in region_tags:
        ftag = tagger.makeforqs_run(region_tag)
        ctags = tagger.make_constructor_tags(ftag, replicate)
        tagger.make_haplotypes(ctags)
        stags = tagger.make_simreads_tags(ctags, pos1, pos2)
        # simreads.index_snps(stags)
        tagger.write_simread_configs(stags)
        simreads.simreads_run(stags)
        simharp.simreads_harp(stags)
        simclean.SimClean()
        tagger.add_simfrequency_attribute(stags)
        tagger.write_frequency_comparison_file(stags)
        tagger.clean_region(stags)
        simharp.fst_whithinreplicate(stags)


if __name__ == '__main__':
    pass
    # # trial[0]
    # ftest = tagger.makeforqs_run(trial[0])
    # ctest = tagger.make_constructor_tags(ftest, 'A')
    # tagger.make_haplotypes(ctest)
    # stest = tagger.make_simreads_tags(ctest)
