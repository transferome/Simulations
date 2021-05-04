"""  Tags Which Package Information for a Replicate Run  """
import simulations.tags.simulationtags as maintags
import simulations.tags.tagconfigs as fconfigtags
import simulations.tags.tagforqs as fproctags
import harpsnp.organize as foundorg
import simulations.tags.constructortags as constructor
import simulations.haptools.generatehaplotypes as generator
import simulations.tags.simreadstag as simtag
import simulations.simulatereads.writeconfig as writer
import simulations.clearregion as clear


def make_tags(chromosome, simulation_number, replicate='A'):
    """Makes tags for the subregions"""
    mytags = maintags.TagMaker(chromosome, simulation_number)
    mytags.create(replicate)
    return mytags.tags


def makeforqs_run(simulation_tag):
    """For each subregion tag, makes tags for the mulitple configs
    from the different multinomial draws at a subregion"""
    fconfigs = fconfigtags.TagConfigs(simulation_tag)
    fconfigs.create_configs()
    fconfigs.list_configs()
    fproc = fproctags.TagForqs(fconfigs)
    fproc.move_configs()
    foundorg.organize(simulation_tag)
    return fproc


def make_constructor_tags(forqsproc_tag, replicate='A'):
    """Makes the sub constructor tags for each forqs proc tag, which has multiple
    forqs process, and thus multiple forqs population file to construct haplotypes from"""
    return constructor.construct_taglist(forqsproc_tag, replicate)


def make_haplotypes(construct_tags):
    """Makes haplotypes for simulatereads to process using the constructor tags"""
    for tag in construct_tags:
        generator.generate(tag)


def make_simreads_tags(construct_tags, pos1, pos2):
    """Makes the tags for simulatereads process which will now happen on the
    created hapotypes generated from the above function"""
    simreads_tag_list = list()
    for tag in construct_tags:
        simreads_tag_list.append(simtag.SimreadsTag(tag, pos1, pos2))
    return simreads_tag_list


def write_simread_configs(simreads_tags):
    for tag in simreads_tags:
        writer.simreads_config(tag)


def add_simfrequency_attribute(simreads_tags):
    for tag in simreads_tags:
        tag.get_simulated_frequencies()


def write_frequency_comparison_file(simreads_tags):
    for idx, tag in enumerate(simreads_tags):
        if not idx:
            with open(tag.final_frequency_file, 'w+') as outfile:
                outfile.write(tag.founding_frequency)
                outfile.write(tag.simulated_frequency)
        else:
            with open(tag.final_frequency_file, 'a') as appendfile:
                appendfile.write(tag.simulated_frequency)


def clean_region(simreads_tags):
    clear.clear_directories()
    clear.clear_foundandsample(simreads_tags)
    clear.clear_simfreqs(simreads_tags)


if __name__ == '__main__':
    pass
