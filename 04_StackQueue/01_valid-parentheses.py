# https://leetcode.com/problems/valid-parentheses/description/
# 괄호로 된 입력값이 올바른지 판별하라. (245 page)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

def isValid(s):
    stack = []
    table = { ')': '(',
              '}': '{',
              ']': '['
            }
    
    for char in s:
        if char not in table: 
            # ( { [ 에 해당 
            stack.append(char)

            # ) } ] 에 해당
            # 무조건 둘이 쌍으로 붙어있어야 함 
            
        elif not stack or table[char] != stack.pop():
            return False
        
    return len(stack) == 0

s = "()[]}"
print(isValid(s))