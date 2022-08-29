def twoSum(numbers, target):
    l = 0
    r = len(numbers)-1
    while l < r:
        curSum = numbers[l] + numbers[r]
        if curSum > target:
            r -=1
        elif curSum < target:
            l+=1
        elif curSum == target:
            good = [l,r]
            return good


numbers = [2,3,4]
#numbers = [-1,0]
target = -1

twoSum(numbers,target)

# for i in range(0,len(numbers)-1):
#     print(f"{i} loop")
#     for j in range(i+1,len(numbers)):
#         print(i)
#         print(numbers[i])
#         print(numbers[j])
#         if numbers[i] + numbers[j] == target:
#             print("Found it.")
#             good = [i+1,j+1]
#             print(good)