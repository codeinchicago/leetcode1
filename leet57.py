"""
Had a coding assessment on Tuesday, 6 September 2022, code did not fit all the test cases. Doing this question to rectify that.


Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

"""

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]

def largest_subarray(nums):
    largest = nums[0] #Cannot have 0 as starting number because all numbers can be negative
    total = 0

    for i in nums:
        total += i
        
        largest = max(largest,total) #Using max rather than comparing and reassigning largest = total saves a line of code

        if total < 0: #Resetting total to 0 is the breakthrough, if sum is negative, then we would want to start subarray over from the next number
            total = 0

    return largest

#print(largest_subarray(nums))