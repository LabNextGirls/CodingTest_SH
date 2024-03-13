# https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    indexes = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i] + nums[j] == target):
                indexes.append([i, j])

    return indexes[0::2]

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

# in을 활용한 풀이 
# target - n 값이 존재하는지 check 

def twoSum2(nums, target):
    indexes = []

    for i, n in enumerate(nums):
        complement = target - n

        # 탐색 범위를 i 번째 인덱스 이후로 
        if complement in nums[i + 1:]:
            indexes.append(nums.index(n), nums[i+1:].index(complement) + i + 1 )

    return indexes[0::2]

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

