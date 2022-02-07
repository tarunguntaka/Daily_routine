
# nums Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#A subarray is a contiguous part of an array

def Maxsubarray(nums):
    
    currsum = maxsum = nums[0]
    for i in nums[1:]:
        currsum = max(i,currsum+i)
        maxsum = max(currsum,maxsum)
    
    return maxsum

nums = [1,2,-3,4,5,-6,5,4,3,-4]

print(Maxsubarray(nums))


# dynamic programming problems have these max and min functions in common 
