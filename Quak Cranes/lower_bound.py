import numpy as np

def lower_bound(n_container, handling_capacity_shift,max_cran_one_time):
    total_no_qack_Crane = 0
    min_shift = 0
    pattern = 0;
    if n_container/(max_cran_one_time * handling_capacity_shift) > int(n_container/(max_cran_one_time * handling_capacity_shift)):
        min_shift = int(np.floor(n_container/(max_cran_one_time * handling_capacity_shift)) + 1);
        extra_var = 1
    else:
        min_shift = int(n_container/(max_cran_one_time * handling_capacity_shift));
        extra_var = 0
    if extra_var == 1:
        extra_con = n_container - (min_shift - 1) * handling_capacity_shift * max_cran_one_time
        if extra_con/handling_capacity_shift > int(extra_con/handling_capacity_shift):
            extra_cranes = int(extra_con/handling_capacity_shift) + 1
        else:
            extra_cranes = extra_con/handling_capacity_shift
        total_no_qack_Crane = int((min_shift-1) * max_cran_one_time) + extra_cranes
        pattern = np.ones(min_shift,dtype=np.int32) * max_cran_one_time;
        pattern[min_shift-1] = extra_cranes
    else:
        total_no_qack_Crane = int(min_shift * max_cran_one_time);
        pattern = np.ones(min_shift,dtype=np.int32) * max_cran_one_time;
    return total_no_qack_Crane, min_shift, pattern;