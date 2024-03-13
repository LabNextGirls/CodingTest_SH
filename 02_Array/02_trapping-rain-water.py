# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라
# https://leetcode.com/problems/trapping-rain-water/description/

def trap(height):
    max_water = 0
    temp_ptr = 0
    max_ptr = height.index(max(height))

    for i in range(len(height)-1):
        # 상승단차 
        if (height[i] < height[i+1]):
            if (height[temp_ptr] < height[i+1]):
                temp_ptr = i + 1
            elif (height[temp_ptr] > height[i+1]):
                max_water += (height[temp_ptr] - height[i+1])
        
        # 하강단차 
        elif (height[i] > height[i+1]):
            if (height[temp_ptr] >= height[i] and (temp_ptr != max_ptr)):
                max_water += (height[temp_ptr] - height[i+1])
            elif (height[temp_ptr] < height[i] and (i != max_ptr)):
                temp_ptr = i
                max_water += (height[i] - height[i+1])

    return max_water

heights = [4,2,0,3,2,5]
print(trap(heights))