def twoSum(numbers, target):
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            print(i)
            print(numbers[i])
            print(numbers[j])
            if numbers[i] + numbers[j] == target:
                good = [i+1,j+1]
                return good




#numbers = [2,3,4]
numbers = [-1,0]
target = -1

# for num in numbers:
#     print(num)
#     count = 1
#     if numbers[num] + numbers[num+count] == target:
#         print(num)

for i in range(0,len(numbers)-1):
    print(f"{i} loop")
    for j in range(i+1,len(numbers)):
        print(i)
        print(numbers[i])
        print(numbers[j])
        if numbers[i] + numbers[j] == target:
            print("Found it.")
            good = [i+1,j+1]
            print(good)

