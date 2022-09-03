# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [3,2,4]
target = 6

#Good candidate for left and right

#Get number, then check other numbers

#Easy checking numbers with set

checking = set(nums)

def finder(nums,target):
    for i in nums:
        #print(f"i: {i}")
        goal = target - i
        #print(f"Goal: {goal}")
        if goal in checking:
            #print("Found.")
            num2 = nums.index(goal)
            return [nums.index(i), num2]

print(finder(nums,target))