import numpy as np
from patterns import *
import os

os.system('cls' if os.name == 'nt' else 'clear')


n_container = int(input("\n\nEnter the Number of Container in the Vessel\n\n"))
handling_capacity_shift = int(input("\n\nEnter the Handling Capacity of the Quak Crane for a shift\n\n"))
hours_shift = int(input("\n\nEnter the Hours in a Shift\n\n"))
max_crane_in_shift = int(input("\n\nEnter the Maximum Number of Cranes in a Shift\n\n"))
time_stay = int(input("\n\nEnter the time which will vessel will stay\n\n"))

total_no_quak_crane, min_shift, pattern_lower = lower_bound(n_container, handling_capacity_shift,max_crane_in_shift);
print("\n\n Total Number of Quak Cranes Required = {}\n\n".format(total_no_quak_crane))
print("\n\n Pattern for Lower Bound = {}\n\n".format(pattern_lower))

pattern_upper = upper_bound(n_container, handling_capacity_shift, max_crane_in_shift,time_stay, hours_shift)
print("\n\n Pattern for Upper Bound = {}\n\n".format(pattern_upper))

patterns = all_possible_patterns(max_crane_in_shift, time_stay, hours_shift, total_no_quak_crane, pattern_lower)
print("\n\n All the Patterns \n\n")
print(patterns)