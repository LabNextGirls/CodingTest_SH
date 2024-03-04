from typing import List

def reverse_list(list):
    list.reverse()
    return list

first = ["h", "e", "l", "l", "o"]
print(reverse_list(first))
# ['o', 'l', 'l', 'e', 'h']

# 다른 풀이 - 투 포인터 활용

def reverseString(s: List[str]): 
    left, right = 0, len(s) -1
    
    while left < right:
        s[left], s[right] = s[right], s[left] 
        left +=1
        right -= 1

    return s

print(reverseString(first))
