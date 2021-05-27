import coverage.windowcoverage as depthtest
import coverage.meancoverage as meancov
import glob
# import coverage.listcovfiles as lister
# import mytime.timer as timer


def subset_snp_coverage_by_window(contig, pos1, pos2):
    contig_list, bed_list = depthtest.make_beds(contig, pos1, pos2)
    depthtest.samtools_depth_multi(contig_list, bed_list)


def list_sample_coverage_windows(sample, contig, pos1, pos2):
    cov_window_files = glob.glob(f'results/{contig}_{pos1}-{pos2}/coverage/{sample}_*.coverage')
    cov_window_files.sort(key=lambda x: int(x.split('/')[-1].split('_')[-1].split('-')[0]))
    return cov_window_files


def mean_coverage_write(contig, pos1, pos2):
    samples = [f'S{_}' for _ in range(1, 11)] + ['S21', 'S22']
    samples_data_super_list = dict()
    samples_windows_super_list = dict()
    for sample in samples:
        samples_data_sub_list = list()
        samples_windows_sub_list = list()
        coverage_files = list_sample_coverage_windows(sample, contig, pos1, pos2)
        for file in coverage_files:
            window = file.split('/')[-1].split('_')[-1].split('.coverage')[0]
            samples_windows_sub_list.append(window)
            mean, var = meancov.get_coverage_mean(file)
            samples_data_sub_list.append(f'{mean},{var}')
        samples_data_super_list[sample] = samples_data_sub_list
        samples_windows_super_list[sample] = samples_windows_sub_list
    same_windows_check = meancov.window_region_check(samples_windows_super_list)
    if not all(same_windows_check):
        print('Different samples have different regions, why?')
        quit()
    else:
        sample_line = [f'S{_}_mean,S{_}_var' for _ in range(1, 11)] + ['S21_mean,S21_var', 'S22_mean,S22_var\n']
        header_line = f"Region,{','.join(sample_line)}"
        coverage_info = [val for val in samples_data_super_list['S1']]
        windows_add = [win for win in samples_windows_super_list['S1']]
        for sample in samples[1:]:
            sample_data = samples_data_super_list[sample]
            for idx, document in enumerate(coverage_info):
                coverage_info[idx] = ','.join([document, sample_data[idx]])
        add_new_line = [f"{win},{s}\n" for win, s in zip(windows_add, coverage_info)]
        with open(f'results/{contig}_{pos1}-{pos2}/SNP_coverage.txt', 'w+') as output:
            output.write(header_line)
            for line in add_new_line:
                output.write(line)
            

if __name__ == '__main__':
    # function_time = timer.Timer()
    cont = '3R'
    posa = 4200000
    posb = 32073015
    samp = 'S1'
    mean_coverage_write(cont, posa, posb)

    # lister.listsubsetcov('S1', cont, posa, posb)
    # subset_snp_coverage_by_window(cont, posa, posb)
    # function_time.stop()
    # print(function_time.elapsed)
