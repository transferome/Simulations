import coverage.windowcoverage as depthtest
import mytime.timer as timer


if __name__ == '__main__':
    # function_time = timer.Timer()
    cont = '3R'
    posa = 4200000
    posb = 32073015
    bed_windows = depthtest.make_beds(cont, posa, posb)
    test_list = depthtest.samtools_depth_commands(bed_windows)
    # function_time.stop()
    # print(function_time.elapsed)
