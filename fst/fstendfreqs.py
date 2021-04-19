"""  Creates Zip Combinations of the Fst Comparisons Between the
  Estimated Frequencies of the DGRP at Generation 15 in the Experimental Data"""
import fst.fstcalculate as fstcalc

comp1 = ['endGen15Up1A_frequencies.txt', 'endGen15Dwn1A_frequencies.txt', 'Exp_Up1A_Dwn1A']
comp2 = ['endGen15Up2A_frequencies.txt', 'endGen15Dwn2A_frequencies.txt', 'Exp_Up2A_Dwn2A']
comp3 = ['endGen15Up1B_frequencies.txt', 'endGen15Dwn1B_frequencies.txt', 'Exp_Up1B_Dwn1B']
comp4 = ['endGen15Up2B_frequencies.txt', 'endGen15Dwn2B_frequencies.txt', 'Exp_Up2B_Dwn2B']
comp5 = ['endGen15CtrlA_frequencies.txt', 'endGen15CtrlB_frequencies.txt', 'Exp_CtrlA_CtrlB']
compUpA = ['endGen15Up1A_frequencies.txt', 'endGen15Up2A_frequencies.txt', 'Exp_Up1A_Up2A']
compDwnA = ['endGen15Dwn1A_frequencies.txt', 'endGen15Dwn2A_frequencies.txt', 'Exp_Dwn1A_Dwn2A']
compUpB = ['endGen15Up1A_frequencies.txt', 'endGen15Up2A_frequencies.txt', 'Exp_Up1B_Up2B']
compDwnB = ['endGen15Dwn1B_frequencies.txt', 'endGen15Dwn2B_frequencies.txt', 'Exp_Dwn1B_Dwn2B']
compctrl1 = ['endGen15Up1A_frequencies.txt', 'endGen15CtrlA_frequencies.txt', 'Exp_Up1A_CtrlA']
compctrl2 = ['endGen15Up2A_frequencies.txt', 'endGen15CtrlA_frequencies.txt', 'Exp_Up2A_CtrlA']
compctrl3 = ['endGen15Dwn1A_frequencies.txt', 'endGen15CtrlA_frequencies.txt', 'Exp_Dwn1A_CtrlA']
compctrl4 = ['endGen15Dwn2A_frequencies.txt', 'endGen15CtrlA_frequencies.txt', 'Exp_Dwn2A_CtrlA']
compctrl5 = ['endGen15Up1B_frequencies.txt', 'endGen15CtrlB_frequencies.txt', 'Exp_Up1B_CtrlB']
compctrl6 = ['endGen15Up2B_frequencies.txt', 'endGen15CtrlB_frequencies.txt', 'Exp_Up2B_CtrlB']
compctrl7 = ['endGen15Dwn1B_frequencies.txt', 'endGen15CtrlB_frequencies.txt', 'Exp_Dwn1B_CtrlB']
compctrl8 = ['endGen15Dwn2B_frequencies.txt', 'endGen15CtrlB_frequencies.txt', 'Exp_Dwn2B_CtrlB']

comparisons = [comp1, comp2, comp3, comp4, comp5, compUpA, compDwnA, compUpB, compDwnB,
               compctrl1, compctrl2, compctrl3, compctrl4, compctrl5, compctrl6, compctrl7,
               compctrl8]


def fst_end(comparison):
    """Takes two Generation 15 files and calculates Fst between certain treatments"""
    outdata = list()
    with open(comparison[0]) as fileA, open(comparison[1]) as fileB:
        data = [line.rstrip('\n') for line in fileA]
        datb = [line.rstrip('\n') for line in fileB]
        for x, y in zip(data, datb):
            infoa = x.split(',')[0]
            infob = x.split(',')[0]
            if infoa == infob:
                freqsa = x.split(',')[1:]
                freqsb = y.split(',')[1:]
                fst_val = fstcalc.fst(freqsa, freqsb)
                outdata.append('{},{}\n'.format(infoa, str(fst_val)))
            else:
                print('Mismatch')
    return outdata


def write_end(comparison):
    """writes out the fst info after its been calculated"""
    fstdata = fst_end(comparison)
    with open('{}_Fst.dat'.format(comparison[2]), 'w+') as outputfile:
        for line in fstdata:
            outputfile.write(line)


def endfst():
    for comp in comparisons:
        write_end(comp)


if __name__ == '__main__':
    pass
