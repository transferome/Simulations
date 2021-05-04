"""Functions to handle simulatereads aspect of a """
import simulations.simulatereads.indexsnptable as indexer
import simulations.simulatereads.simreadsparallel as simparallel
import simulations.simulatereads.samtoolschangeheader as header
# import simulations.simulatereads.samtoolsviewparallel as view
# import simulations.simulatereads.samtoolssortparallel as sorter
import simulations.simulatereads.samtoolsviewsort as samtool
import simulations.simulatereads.samtoolsindexparallel as sindex
import simulations.simulatereads.cleansimreads as simcleaner


def index_snps(simreads_tags):
    """Index the snp tables created for runnings simulatereads, these are the
    haplotype .txt files attached to the simulatereads tags"""
    indexer.index_snp_multi(simreads_tags)


def simreads_parallel(simreads_tags):
    """Given a set of constructor_tags, runs simulatereads in parallel
    All constructor tags given when function called should have same region tag
    function returns a region tag from one of the constructor tags
    which is then passed to the simreads_process function"""
    simparallel.simreads_multi(simreads_tags)
    return simreads_tags[0].region_tag


def simreads_process(simread_tag_region_tag):
    header.samtools_change_multi(simread_tag_region_tag)
    # view.samtools_view_multi(simread_tag_region_tag)
    # sorter.samtools_sort_multi(simread_tag_region_tag)
    samtool.samtools_view_multi(simread_tag_region_tag)
    sindex.samtools_index_multi(simread_tag_region_tag)
    simcleaner.removesams(simread_tag_region_tag)
    # simcleaner.removebams(simread_tag_region_tag)
    simcleaner.movefreqs(simread_tag_region_tag)


def simreads_run(simreads_tags):
    sim_reg_tag = simreads_parallel(simreads_tags)
    simreads_process(sim_reg_tag)


if __name__ == '__main__':
    pass
