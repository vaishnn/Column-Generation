import numpy as np
from lower_bound import lower_bound

def upper_bound(n_container, handling_capacity_shift,max_cran_one_time,time_stay,hours_shift):
    total_no_crane,_,_ = lower_bound(n_container, handling_capacity_shift,max_cran_one_time);
    no_cranes_per_shift = (total_no_crane / time_stay) * hours_shift;
    pattern = 0
    if no_cranes_per_shift < 1:
        pattern = np.zeros(int(time_stay/hours_shift))
        for i in range(int(total_no_crane)):
            pattern[i] = 1;
    else:
        if no_cranes_per_shift > int(no_cranes_per_shift):
            pattern = int(no_cranes_per_shift) * np.ones(int(time_stay/hours_shift))
            pattern[int(time_stay/hours_shift)-1] += total_no_crane - sum(pattern);
        else:
            pattern = int(no_cranes_per_shift) * np.ones(int(time_stay/hours_shift))     

    return pattern   
