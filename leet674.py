"""
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
"""

nums = [1,3,5,4,7]
#nums = [2,2,2,2,2]
#nums = [1,3,5,4,2,3,4,5]

def increasing(nums):
    if len(nums) == 1: #If length of list is 1, no increasing sequence
        return 1
    length = 1
    longest = 1
    for i in range(1,len(nums)): #Starting at 1 b/c that way I can check the current number to previous number
        #print(nums[i],nums[i-1])
        if nums[i] > nums[i-1]:
            length += 1
            #print(f"This is a new chain of {length}")
            longest = max(length,longest)
        else:
            length = 1
    #print(longest)
    return longest
    
increasing(nums)