# https://leetcode.com/problems/product-of-array-except-self/description/
from math import prod

def productExceptSelf(nums):
    ans_list = []
    whole_product = prod(nums)

    for i in range(len(nums)):
        if (nums[i] != 0): 
            ans_list.append(int(whole_product/nums[i]))
        else:
            temp = nums.copy()
            del temp[i]
            ans_list.append(prod(temp))

    return ans_list

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))