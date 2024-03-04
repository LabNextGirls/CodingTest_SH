import re

def isPalindrome(str):
    new_str = re.sub(r"[^a-zA-Z]", "", str)
    new_str = new_str.lower()

    str_list = list(new_str)
    str_list.reverse()

    if (list(new_str) == str_list):
        isPalindrome = True
    else:
        isPalindrome = False

    return isPalindrome

first = "A man, a plan, a canal: Panama"
second = "race a car"

print(isPalindrome(first))
print(isPalindrome(second))


# 답안

def isPalindrome(self, s: str) -> bool:
    strs = []
    
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
            
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop(): 
            return False
    
    return True
