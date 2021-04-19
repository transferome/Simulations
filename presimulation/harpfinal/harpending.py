"""  Calculating Generation 15 freqs for a blueprint """
import harpsnp.harp_gen15like as hlk
import harpsnp.harp_freq as freq
import harpsnp.harpclean as cleaner


def clean(blueprint):
    """Cleans up the files"""
    cleaner.HarpEndClean(blueprint)


class HarpEnd:
    """Runs harp on the Generation 15 files and cleans up"""

    def __init__(self, blueprint):
        """Takes in the original window to read the blueprint and estimate
        frequencies along that window"""
        self.contig = blueprint.chromosome
        self.window = blueprint.window
        self.region_size = blueprint.region_size
        # start harp a bit upstream and downstream
        self.region = '{}:{}-{}'.format(self.contig,
                                            str(self.window[0] - round(self.region_size * 0.25)),
                                            str(self.window[1] + round(self.region_size * 0.25)))

    def like(self):
        hlk.like_multi(self.contig, self.region)

    def freq(self, width):
        freq.freq_multi(self.region, width, gen='Gen15')


if __name__ == '__main__':
    pass
