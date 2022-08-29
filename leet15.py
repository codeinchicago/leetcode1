# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         pass


nums = [-1,0,1,2,-1,-4]

if -8 in nums:
    print("Yes")

#Removing duplicates
slim = set(nums)
listed = sorted(list(slim))
print(listed)

for i in range(0,len(nums)-1):
    count = 0
    pass