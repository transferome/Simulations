import coverage.windowcoverage as depthtest
import time


if __name__ == '__main__':
    begin = time.time()
    cont = '2R'
    posa = 4200000
    posb = 25258235
    depthtest.dgrp_coverage_files(cont, posa, posb)
    end = time.time()
    print(end - begin)



