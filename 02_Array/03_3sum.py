# https://leetcode.com/problems/3sum/description/

def threeSum(nums):
    ans_list = []

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if -1 * (nums[i] + nums[j]) in nums[j+1::]:
                ans_list.append([nums[i], nums[j], -1 * (nums[i] + nums[j])])

    return ans_list[::3]

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))


'''

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

'''