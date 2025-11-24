import numpy as np

def count_values_in_bins(data, bin_edges):
    
    Bins = len(bin_edges) - 1
    
    counts = np.zeros(Bins, dtype=int)
    
    
    for value in data:
        if value < bin_edges[0] or value > bin_edges[-1]:
            continue
        
        for i in range(Bins):
            left = bin_edges[i]
            right = bin_edges[i + 1]
            
            
            if i < Bins - 1:
                if value >= left and value < right :
                    counts[i] += 1
                    break
                
            else:
                if value >= left and value <= right:
                    counts[i] += 1
                    break
                
                
    return counts

#%% explanation of the code for reference follows

# first we define a function that takes two inputs (both being arrays)
# one an array of numbers we want to sort, and then another which includes
# the edges of the bins

#we then count how many bins there are with length -1
# we then initialize an array called counts with length of Bins (one spot for)
# (each bin) and setting the values to be integers

# now we create a loop over all numbers in data and first check if the value 
# is outside the entire range of bins (to the left of the leftmost bin and
# to the right of the rightmost bin) and if so we choose to ignore it

# now we loop over each bin index of i, i.e. if there are 3 bins then we have 
# 0,1,2 as i's. and then we check for each bin what its left and right edge is.
# we then continue first checking if we are in the last bin, and if we are not
# we then check if the value is in the current bin, if so we add a count
# and we stop checking other bins

#then for the last bin, we check if its in the last bin (inclusive right) and if 
# so we add a count 

# we then return a count array