import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):

    cleaned_array = scores.copy()
    
    cleaned_array[cleaned_array < min_score] = min_score
    cleaned_array[cleaned_array > max_score] = max_score
    
    scaled_array = (cleaned_array - min_score) / (max_score - min_score)
    
    return scaled_array

#%%
#Quick explanation of code for reference

# we defined a function taking three inputs, an array of scores, the lowest
# allowed score and the largest allowed score
# we then make a copy of said score array which we can work on without altering
# the original

# we then create a boolean mask to select all scores less than our min score
# and then we replace that score with our min score

# we do the same for the max score

# we then scale the array to be a number between 0 and 1
# first subtracting the min score from all cleaned values
# then dividing each value by the range of allowed scores

# then returning an array with all values 0-1