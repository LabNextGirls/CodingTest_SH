# https://leetcode.com/problems/array-partition/description/

def arrayPairSum(nums):
    answer = 0
    sort = sorted(nums)
    print(sort)

    for i in range(1, len(sort), 2):
        answer += sort[-1 * (i + 1)]
        print(answer)
    return answer

nums = [1,4,3,2]
print(arrayPairSum(nums))