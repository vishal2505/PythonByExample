# Given an unsorted list and a number S, 
# find all the pairs of numbers in that list such that their sum equals S.

def twoSumHashing(num_arr, pair_sum):
    hash_table={}
    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hash_table:
            print("pairs : ({},{}) which have sum as {}".format(complement,num_arr[i],pair_sum))
        hash_table[num_arr[i]]=num_arr[i]

# Driver Code
num_arr = [3, 5, 2, -4, 8, 11]
pair_sum = 7    
  
# Calling function
twoSumHashing(num_arr, pair_sum)

#Output
#pairs : (5,2) which have sum as 7
#pairs : (-4,11) which have sum as 7
