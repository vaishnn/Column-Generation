import numpy as np
from upper_bound import upper_bound
from lower_bound import lower_bound

#For Calculating all possible patterns and then storing it in the array
def all_possible_patterns(max_crane_in_one_time, time_stay, hours_shift, total_no_of_quack_crane, pattern_lower):
    pattern = np.array([[]]);
    pattern_lower = np.transpose(np.append(pattern_lower, np.zeros(int(time_stay/hours_shift) - np.shape(pattern_lower)[0])))
    pattern = np.append(pattern, np.reshape(pattern_lower, [1,np.shape(pattern_lower)[0]]))
    pattern = np.reshape(pattern,[1,pattern.shape[0]])
    new_patterns = np.array(generate_patterns(time_stay/hours_shift, max_crane_in_one_time, total_no_of_quack_crane))
    for i in new_patterns:
        if check_replicacy(pattern, i) == 1:
            pattern = np.append(pattern, np.reshape(np.sort(i)[::-1], [1,np.shape(i)[0]]),axis=0)

        else:
            continue
    return pattern

    
# For generating patterns
def generate_patterns(n, k, m, pattern=[]):
    patterns = []  

    if len(pattern) == n:  
        if sum(pattern) == m:  
            patterns.append(pattern.copy())
        return patterns
    
    for i in range(k + 1): 
        if sum(pattern) + i <= m: 
            patterns += generate_patterns(n, k, m, pattern + [i]) 

    return patterns

# To check if the pattern generated is already been generated or not
def check_replicacy(pattern,new_r):
    
    for i in range(np.shape(pattern)[0]):
        if np.array_equal(np.sort(pattern[i,:]), np.sort(new_r)):
            return -1
    return 1