import numpy as np

def moving_average(signal, window_size):
   
    n = len(signal)
    k = (window_size - 1) // 2
    
    result = np.zeros(n)
    
    for i in range(n):
        start = i - k
        if start < 0:
            start = 0
            
        end = i + k 
        if end > n - 1:
            end = n - 1
            
        total = 0.0
        count = 0
        for j in range(start, end + 1):
            total += signal[j]
            count += 1
            
            
        result[i] = total / count
        
    return result
#%%
# explanation for reference

# we first define a function that takes two inputs, one being an array of numbers and another being an odd number
# telling you how many values to average around each position. the function will then return signal

# first we set n to be how many elements are in the array

# we then compute k which  is how many steps to the right and left we want to take so if window_size = 3, then 1 to the left
# and 1 to the right via integer division

# we set a result array with n zeros in it (same length as signal)

# now we start a loop over each i in the signal, with i  being 0,1,2,3,4. we 
# start the window k before i, and we check if that is negative and we bind it to 0 if so

# which is done for the same thing on the right side as well binding it to n-1

# we then total to 0 (summation) and count to 0 (number of values added)

# then a second loop over the indices inside the window we made earlier
# we check the value at that position and add the value to total then for how
# many values were added that becomes count, then the new value at i is 
# total/count i.e. the average in that window,
# this is then done for each i in signal. 

#we then get a result array 